"""LangGraph single-node graph template.

Returns a predefined response. Replace logic and configuration as needed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, TypedDict, List
import json
import os

from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph


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
    questions: List[dict]
    current_count: int
    batch_size: int = 100
    target_count: int = 1000


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

def mock_generate_questions_for_topic(topic, num_questions, start_index):
    """Mock function to generate questions for a specific topic."""
    return [
        {
            "id": start_index + i,
            "question": f"Mock {topic} Question {start_index + i + 1}",
            "choices": ["A", "B", "C", "D"],
            "answer": "A",
            "explanation": f"Explanation for {topic} question {start_index + i + 1}"
        }
        for i in range(num_questions)
    ]

async def generate_all_by_topic(state: State, config: RunnableConfig) -> dict:
    """Generate 100 questions for each topic, grouped by topic."""
    questions_by_topic = {}
    idx = 0
    for topic in topics:
        qs = mock_generate_questions_for_topic(topic["name"], QUESTIONS_PER_TOPIC, idx)
        questions_by_topic[topic["name"]] = qs
        idx += QUESTIONS_PER_TOPIC
    return {
        "questions": questions_by_topic,
        "current_count": idx,
        "batch_size": state.batch_size,
        "target_count": state.target_count,
    }

async def check_completion_by_topic(state: State, config: RunnableConfig) -> str:
    if state.current_count >= state.target_count:
        write_to_json(state.questions)
        return "end"
    return "generate_all_by_topic"

def write_to_json(questions_by_topic: dict, filename: str = "step_questions.json"):
    """Write questions grouped by topic to a JSON file in the project root."""
    path = os.path.join(os.path.dirname(__file__), "..", "..", filename)
    with open(os.path.abspath(path), "w") as f:
        json.dump(questions_by_topic, f, indent=2)

# Define the graph
graph = StateGraph(State)
graph.add_node("generate_all_by_topic", generate_all_by_topic)
graph.add_node("check_completion_by_topic", check_completion_by_topic)
graph.add_edge("__start__", "generate_all_by_topic")
graph.add_edge("generate_all_by_topic", "check_completion_by_topic")
graph.add_conditional_edges(
    "check_completion_by_topic",
    {
        "generate_all_by_topic": "generate_all_by_topic",
        "end": None,
    },
)
graph = graph.compile(name="STEP Question Generator by Topic")
