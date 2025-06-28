"""LangGraph single-node graph template.

Returns a predefined response. Replace logic and configuration as needed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, TypedDict, List, Optional, Literal
import json
import os
import asyncio
from time import sleep

from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from src.agent import topic_prompts

llm = init_chat_model("openai:gpt-4o")


class State(TypedDict):
    """Input state for the agent.

    Tracks progress and stores generated questions.
    """

    topic: Literal[
        "Biochemistry",
        "Genetics",
        "AllergiesAndImmunology",
        "Cardiovascular",
        "Microbiology",
        "Dermatology",
        "Pathology",
        "Pharmacology",
        "EarNoseAndThroat",
        "BiostatsAndEpidemiology",
        "EndocrineAndDiabetesAndMetabolism",
        "PosioningAndEnviromentalExposure",
        "PsychiatricAndSubstanceUseDisorders",
        "SocialSciences",
        "HematologyAndOncology",
        "InfectiousDiseases",
        "MaleReproductiveSystem",
        "NervousSystem",
        "Ophthalmology",
        "PregnancyChildbirthAndPuerperium",
        "CriticalCare",
        "RenalAndUrinary",
        "RheumatologyAndOrthopedics",
    ]
    questions: list[Question]
    answer: any


class Question(BaseModel):
    topic: str = Field(description="The topic of the question.")
    subtopic: str = Field(description="The subtopic of the question.")
    question: str = Field(description="The question text.")
    choices: list[str] = Field(
        description="A list of 5 answer choices.", min_length=5, max_length=5
    )
    answer: str = Field(description="The correct answer, must be one of the choices.")
    explanation: str = Field(description="A detailed explanation for the answer.")


class Questions(BaseModel):
    questions: list[Question] = Field(description="A list of 10 questions.")


DEFAULT_SYSTEM_PROMPT = (
    "You are a medical board exam question writer. "
    "Write a USMLE Step 2 CK-style multiple-choice question for the topic: '{topic}'. "
    "Return ONLY a valid JSON object that matches this schema: {format_instructions}. "
    "The 'choices' field must be a list of exactly 5 answer choices, and the 'answer' must be one of those 5 choices. "
    "Do not include any text except the JSON."
)


def generate_question_with_llm(state: State):
    subtopics = getattr(topic_prompts, state["topic"])
    total_questions: list[Question] = []
    # print(subtopics)
    # subtopics = topic_prompts.Biochemistry
    question_llm = llm.with_structured_output(Questions)
    for subtopic in subtopics:
        print(subtopics[subtopic])
        template_multiple = """You are a medical board exam question writer.
        You are given a topic and a subtopic.
        Topic: {topic}
        SubTopic: {subtopic}
        You are to write a USMLE Step 1 CK-style multiple-choice question for the topic and subtopic.
        You are to generate 10 questions.
        Make sure you generate unique questions
        Make sure the questions differ in patient scenarios.
        Make sure the questions test the patients clinical knowledge.
        Here is the prompt for this subtopic:
        {subtopic_prompt}
        Here is a sample question for this subtopic:
        Sample Question: {sample_question}
        Sample Choices: {sample_choices}
        Sample Answer: {sample_answer}
        Sample Explanation: {sample_explanation}
        
        """
        prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
        setTemplate = prompt_multiple.invoke(
            {
                "topic": state["topic"],
                "subtopic": subtopic,
                "subtopic_prompt": subtopics[subtopic]["prompt"],
                "sample_question": subtopics[subtopic]["sample_question"]["question"],
                "sample_choices": subtopics[subtopic]["sample_question"]["choices"],
                "sample_answer": subtopics[subtopic]["sample_question"]["answer"],
                "sample_explanation": subtopics[subtopic]["sample_question"][
                    "explanation"
                ],
            }
        )
        print(setTemplate)
        answer = question_llm.invoke(setTemplate)
        total_questions.extend(answer.questions)

    # After collecting all questions
    json_ready_questions = [q.model_dump() for q in total_questions]
    topic_json = {state["topic"]: json_ready_questions}
    with open("questions.json", "w") as f:
        json.dump(topic_json, f, indent=2)
    return topic_json


workflow = StateGraph(State)
workflow.add_node("generate_question", generate_question_with_llm)
workflow.add_edge(START, "generate_question")
workflow.add_edge("generate_question", END)
graph = workflow.compile()
