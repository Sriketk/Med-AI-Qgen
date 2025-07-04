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
from agent import topic_prompts_step2
from agent.prompts import template_step2_ck
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

try:
    # MongoDB connection URI (default to localhost)
    mongo_uri = os.getenv("MONGODB_URI")
    client = MongoClient(mongo_uri)
    db = client["Qbank"]
    collection = db["qbanks"]  # Use your desired database name
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
        "BiostatsAndEpidemiology",
        "Cardiovascular",
        "MaleReproductiveSystem",
        "NervousSystem",
        "Dermatology",
        "Ophthalmology" "EarNoseThroatENT",
        "EndocrineDiabetesMetabolism",
        "PosioningAndEnviromentalExposure",
        "PregnancyChildbirthPuerperium",
        "PsychiatricBehavioralAndSubstanceUseDisorder",
        "FemaleReproductiveSystemAndBreast",
        "GastrointestinalAndNutrition",
        "PulmonaryAndCriticalCare",
        "HematologyOncology",
        "AllergyAndImmunology",
        "RenalUrinarySystemsElectrolytes",
        "InfectiousDiseases",
        "RheumatologyOrthopedicsSports",
        "SocialSciencesEthicsLegalProfessional",
    ]
    questions: list[Question]


class PatientDetails(BaseModel):
    medications: list[str] = Field(
        description="List of patient's current medications", default=[]
    )
    allergies: list[str] = Field(
        description="List of patient's known allergies", default=[]
    )
    familyHistory: list[str] = Field(
        description="List of relevant family medical history", default=[]
    )
    labResults: list[str] = Field(
        description="List of laboratory test results", default=[]
    )
    options: list[str] = Field(
        description="List of treatment or diagnostic options", default=[]
    )
    bloodPresure: str = Field(
        description="Patient's blood pressure reading", default=""
    )
    respirations: str = Field(description="Patient's respiratory rate", default="")
    pulse: str = Field(description="Patient's heart rate/pulse", default="")
    physicalExamination: str = Field(
        description="Findings from physical examination", default=""
    )
    temperature: str = Field(description="Patient's body temperature", default="")
    history: str = Field(description="Patient's medical history", default="")
    demographics: str = Field(description="Patient demographic information", default="")


class Question(BaseModel):
    topic: str = Field(description="The topic of the question.")
    subtopic: str = Field(description="The subtopic of the question.")
    patientDetails: PatientDetails = Field(description="Patient details")
    entireQuestion: str = Field(
        description="The question including all of the patient details and all of the details .."
    )
    baseQuestion: str = Field(
        description="The bare context and question of the case. Should be enought to point the user in the right direction. The minimum information for the user to ask a follow up question."
    )
    shelfSubject: Literal[
        "Ambulatory Medicine",
        "Clinical Neurology",
        "Emergency Medicine",
        "Family Medicine",
        "Medicine",
        "OBGYN",
        "Pediatrics",
        "Psychiatry",
        "Surgery",
    ] = Field(description="The shelf subject of the question.")
    choices: list[str] = Field(
        description="A list of 5 answer choices.", min_length=5, max_length=5
    )
    answer: str = Field(description="The correct answer, must be one of the choices.")
    explanation: str = Field(description="A detailed explanation for the answer.")
    source: str = Field(description="The source of the question.")
    created_at: str = Field(description="The date and time the question was created.")
    embedding: list[float] = Field(description="The embedding of the question.")
    examType: str = Field(description="The type of exam the question is for.")


class Questions(BaseModel):
    questions: list[Question] = Field(description="A list of 10 questions.")


def generate_question_with_llm(state: State):
    subtopics = getattr(topic_prompts_step2, state["topic"])
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
        text_to_embed = question.entireQuestion + " " + " ".join(question.choices)
        embedding = embeddings.embed_query(text_to_embed)
        question.embedding = embedding
        question.examType = "Step-2"
    # After collecting all questions
    with open("step2_questions.txt", "w") as f:
        f.write(str(total_questions))
    # collection.insert_many(total_questions)

    return {"questions": total_questions}


workflow = StateGraph(State)
workflow.add_node("generate_question", generate_question_with_llm)
workflow.add_edge(START, "generate_question")
workflow.add_edge("generate_question", END)
graph = workflow.compile()
