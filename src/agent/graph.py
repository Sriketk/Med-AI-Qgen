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

from langgraph.graph import StateGraph
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import PydanticOutputParser
from src.agent import topic_prompts


llm = init_chat_model("openai:gpt-4o")


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




class Step2CKQuestion(BaseModel):
    question: str = Field(..., description="The question text.")
    choices: list[str] = Field(
        ..., min_items=5, max_items=5, description="A list of 5 answer choices."
    )
    answer: str = Field(
        ..., description="The correct answer, must be one of the choices."
    )
    explanation: str = Field(..., description="A detailed explanation for the answer.")


DEFAULT_SYSTEM_PROMPT = (
    "You are a medical board exam question writer. "
    "Write a USMLE Step 2 CK-style multiple-choice question for the topic: '{topic}'. "
    "Return ONLY a valid JSON object that matches this schema: {format_instructions}. "
    "The 'choices' field must be a list of exactly 5 answer choices, and the 'answer' must be one of those 5 choices. "
    "Do not include any text except the JSON."
)

