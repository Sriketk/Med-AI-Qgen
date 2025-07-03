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
from datetime import datetime
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from langchain_core.messages import SystemMessage
from langchain_openai import OpenAIEmbeddings
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from agent import topic_prompts
from prompts import template_step2_ck 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
load_dotenv()

try:
    # MongoDB connection URI (default to localhost)
    mongo_uri = os.getenv("MONGODB_URI")
    client = MongoClient(mongo_uri)
    db = client["Qbank"]
    collection = db["Qbank"]   # Use your desired database name
    print("MongoDB client set up. Database name:", db.name)
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    db = None
    collection = None

llm = init_chat_model("openai:gpt-4.1", temperature=0.7)
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")


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
    source: str = Field(description="The source of the question.")
    created_at: str = Field(description="The date and time the question was created.")
    embedding: list[float] = Field(description="The embedding of the question.")


class Questions(BaseModel):
    questions: list[Question] = Field(description="A list of 10 questions.")


def generate_question_with_llm(state: State):
    subtopics = getattr(topic_prompts, state["topic"])
    total_questions: list[Question] = []
    # print(subtopics)
    # subtopics = topic_prompts.Biochemistry
    question_llm = llm.with_structured_output(Questions)
    for subtopic in subtopics:
        print(subtopics[subtopic])
        prompt_multiple = ChatPromptTemplate.from_template(template_step2_ck)
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
    for question in total_questions:
        question.source = "gpt-4.1"
        question.created_at = datetime.now().isoformat()
        text_to_embed = question.question + " " + " ".join(question.choices)
        embedding = embeddings.embed_query(text_to_embed)
        question.embedding = embedding
    # After collecting all questions
    with open("questions.txt", "w") as f:
        f.write(str(total_questions))

    
    return {"questions": total_questions}


workflow = StateGraph(State)
workflow.add_node("generate_question", generate_question_with_llm)
workflow.add_edge(START, "generate_question")
workflow.add_edge("generate_question", END)
graph = workflow.compile()
