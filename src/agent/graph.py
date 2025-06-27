"""LangGraph single-node graph template.

Returns a predefined response. Replace logic and configuration as needed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, TypedDict, List, Optional
import json
import os
import asyncio
from time import sleep

from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import PydanticOutputParser
from src.agent import topic_prompts


llm = init_chat_model("openai:gpt-4o")


class Configuration(TypedDict):
    """Configurable parameters for the agent.

    Set these when creating assistants OR when invoking the graph.
    See: https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/
    """

    my_configurable_param: str


@dataclass
class State:
    """Input state for the agent.

    Tracks progress and stores generated questions.
    """
    questions: list[dict]
    current_count: int
    topic: str
    subtopics: Optional[list[str]] = None
    subtopic: str = ""
    batch_size: int = 10  # Number of questions per batch
    target_count: int = 10  # Total questions to generate per subtopic
    current_subtopic_index: int = 0


topics = [
    {"name": "General Principles of Foundational Science"},
    {"name": "Immune System"},
    {"name": "Blood & Lymphoreticular System"},
    {"name": "Behavioral Health"},
    {"name": "Nervous System & Special Senses"},
    {"name": "Musculoskeletal System/Skin & Subcutaneous Tissue"},
    {"name": "Cardiovascular System"},
    {"name": "Respiratory System"},
    {"name": "Gastrointestinal System"},
    {"name": "Renal & Urinary System & Male Reproductive"},
    {"name": "Pregnancy, Childbirth & the Puerperium"},
    {"name": "Female Reproductive System & Breast"},
    {"name": "Endocrine System"},
    {"name": "Multisystem Processes & Disorders"},
    {"name": "Biostatistics & Epidemiology/Population Health/Interpretation of Medical Literature"},
    {"name": "Social Sciences: Legal/Ethical Issues & Professionalism/Systems-based Practice & Patient Safety"},
]

QUESTIONS_PER_TOPIC = 100

class Step2CKQuestion(BaseModel):
    question: str = Field(..., description="The question text.")
    choices: list[str] = Field(..., min_items=5, max_items=5, description="A list of 5 answer choices.")
    answer: str = Field(..., description="The correct answer, must be one of the choices.")
    explanation: str = Field(..., description="A detailed explanation for the answer.")

parser = PydanticOutputParser(pydantic_object=Step2CKQuestion)

DEFAULT_SYSTEM_PROMPT = (
    "You are a medical board exam question writer. "
    "Write a USMLE Step 2 CK-style multiple-choice question for the topic: '{topic}'. "
    "Return ONLY a valid JSON object that matches this schema: {format_instructions}. "
    "The 'choices' field must be a list of exactly 5 answer choices, and the 'answer' must be one of those 5 choices. "
    "Do not include any text except the JSON."
)

async def generate_question_with_llm(topic: str, idx: int, config: RunnableConfig) -> dict:
    # Dynamically select the prompt class for the topic
    class_name = (
        topic.replace('&', 'And')
             .replace('/', 'And')
             .replace('-', '')
             .replace(',', '')
             .replace(':', '')
             .replace('(', '')
             .replace(')', '')
             .replace(' ', '') + 'Prompt'
    )
    system_prompt = getattr(topic_prompts, class_name, None)
    if system_prompt is not None:
        prompt_str = system_prompt.SYSTEM_PROMPT
    else:
        prompt_str = DEFAULT_SYSTEM_PROMPT
    prompt = prompt_str.format(topic=topic, format_instructions=parser.get_format_instructions())
    system_message = SystemMessage(content=prompt)
    response = await llm.ainvoke([system_message])
    # Parse the LLM's response using the Pydantic parser
    try:
        data = parser.parse(response.content)
        data = data.model_dump()
    except Exception:
        # If parsing fails, return a fallback format
        data = {
            "question": response.content,
            "choices": ["A", "B", "C", "D", "E"],
            "answer": "A",
            "explanation": "No explanation provided."
        }
    data["id"] = idx
    return data

async def generate_questions_for_topic_with_llm_batched(topic: str, num_questions: int, start_index: int, batch_size: int, config: RunnableConfig) -> list:
    questions = []
    idx = start_index
    while idx < start_index + num_questions:
        batch_end = min(idx + batch_size, start_index + num_questions)
        tasks = [generate_question_with_llm(topic, i, config) for i in range(idx, batch_end)]
        batch_results = await asyncio.gather(*tasks)
        questions.extend(batch_results)
        idx += batch_size
        if idx < start_index + num_questions:
            await asyncio.sleep(2)  # Pause between batches to avoid rate limits
    return questions

async def generate_for_single_subtopic(state: State, config: RunnableConfig) -> dict:
    """Generate questions for the specified subtopic in batches, using the correct prompt string."""
    subtopic = state.subtopics[state.current_subtopic_index]
    # Find the prompt class for the topic
    class_name = (
        state.topic.replace('&', 'And')
            .replace('/', 'And')
            .replace('-', '')
            .replace(',', '')
            .replace(':', '')
            .replace('(', '')
            .replace(')', '')
            .replace(' ', '') + 'Prompt'
    )
    prompt_class = getattr(topic_prompts, class_name, None)
    if prompt_class is None or not hasattr(prompt_class, subtopic):
        raise ValueError(f"No prompt string found for subtopic: {subtopic} in topic: {state.topic}")
    prompt_str = getattr(prompt_class, subtopic)
    async def generate_question_with_custom_prompt(idx: int, config: RunnableConfig) -> dict:
        prompt = prompt_str.format(topic=subtopic, format_instructions=parser.get_format_instructions())
        system_message = SystemMessage(content=prompt)
        response = await llm.ainvoke([system_message])
        try:
            data = parser.parse(response.content)
            data = data.model_dump()
        except Exception:
            data = {
                "question": response.content,
                "choices": ["A", "B", "C", "D", "E"],
                "answer": "A",
                "explanation": "No explanation provided."
            }
        data["id"] = idx
        data["subtopic"] = subtopic
        return data
    questions = []
    idx = 0
    while idx < state.target_count:
        batch_end = min(idx + state.batch_size, state.target_count)
        tasks = [generate_question_with_custom_prompt(i, config) for i in range(idx, batch_end)]
        batch_results = await asyncio.gather(*tasks)
        questions.extend(batch_results)
        idx += state.batch_size
        if idx < state.target_count:
            await asyncio.sleep(2)
    all_questions = state.questions + questions
    return {
        "questions": all_questions,
        "current_count": len(all_questions),
        "topic": state.topic,
        "subtopics": state.subtopics,
        "subtopic": subtopic,
        "batch_size": state.batch_size,
        "target_count": state.target_count,
        "current_subtopic_index": state.current_subtopic_index + 1,
    }

async def judge_diversity(state: State, config: RunnableConfig) -> dict:
    """Judge and filter out similar questions within each subtopic for diversity."""
    from difflib import SequenceMatcher
    filtered_questions = []
    for subtopic in state.subtopics:
        subtopic_questions = [q for q in state.questions if q.get("subtopic") == subtopic]
        unique_questions = []
        for q in subtopic_questions:
            if all(SequenceMatcher(None, q["question"], uq["question"]).ratio() < 0.8 for uq in unique_questions):
                unique_questions.append(q)
        filtered_questions.extend(unique_questions)
    return {
        **state.__dict__,
        "questions": filtered_questions
    }

async def check_completion_subtopics(state: State, config: RunnableConfig) -> dict:
    if state.current_subtopic_index >= len(state.subtopics):
        return {"next": "judge_diversity"}
    return {"next": "generate_for_single_subtopic"}

async def check_completion_single_topic(state: State, config: RunnableConfig) -> dict:
    if state.current_count >= state.target_count:
        await asyncio.to_thread(write_to_json, state.questions)
        return {"next": "end"}
    return {"next": "generate_for_single_subtopic"}

def write_to_json(questions: list, filename: str = "step_questions.json"):
    """Write questions to a JSON file in the project root."""
    path = os.path.join(os.path.dirname(__file__), "..", "..", filename)
    with open(os.path.abspath(path), "w") as f:
        json.dump(questions, f, indent=2)

async def initialize_subtopics(state: State, config: RunnableConfig) -> dict:
    """Initialize subtopics from the topic if not already set, using ALL_CAPS class attributes as subtopics."""
    if state.subtopics is not None:
        return state.__dict__
    # Dynamically select the prompt class for the topic
    class_name = (
        state.topic.replace('&', 'And')
            .replace('/', 'And')
            .replace('-', '')
            .replace(',', '')
            .replace(':', '')
            .replace('(', '')
            .replace(')', '')
            .replace(' ', '') + 'Prompt'
    )
    prompt_class = getattr(topic_prompts, class_name, None)
    if prompt_class is None:
        raise ValueError(f"No prompt class found for topic: {state.topic}")
    # Use all ALL_CAPS class attributes as subtopics
    subtopics = [attr for attr in dir(prompt_class) if attr.isupper() and not attr.startswith('__')]
    if not subtopics:
        raise ValueError(f"No ALL_CAPS subtopic attributes found for topic: {state.topic}")
    return {
        **state.__dict__,
        "subtopics": subtopics,
    }

# Define the graph
graph = StateGraph(State)
graph.add_node("initialize_subtopics", initialize_subtopics)
graph.add_node("generate_for_single_subtopic", generate_for_single_subtopic)
graph.add_node("judge_diversity", judge_diversity)
graph.add_node("check_completion_subtopics", check_completion_subtopics)
graph.add_node("check_completion_single_topic", check_completion_single_topic)
graph.add_edge("__start__", "initialize_subtopics")
graph.add_edge("initialize_subtopics", "generate_for_single_subtopic")
graph.add_edge("generate_for_single_subtopic", "check_completion_subtopics")
graph.add_conditional_edges(
    "check_completion_subtopics",
    {
        "generate_for_single_subtopic": "generate_for_single_subtopic",
        "judge_diversity": "judge_diversity",
    },
)
graph.add_edge("judge_diversity", "check_completion_single_topic")
graph.add_conditional_edges(
    "check_completion_single_topic",
    {
        "generate_for_single_subtopic": "generate_for_single_subtopic",
        "end": None,
    },
)
graph = graph.compile(name="STEP Question Generator Subtopics")

