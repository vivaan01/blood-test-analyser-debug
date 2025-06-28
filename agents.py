"""
Blood Test Report Analyser - AI Agents Configuration
==================================================

This module defines the AI agents used in the blood test analysis system.
Each agent has a specific role in analyzing blood test reports and providing
comprehensive health recommendations.

Agents:
- Doctor: Main medical analyst for blood test interpretation
- Verifier: Document verification specialist
- Nutritionist: Clinical nutrition expert
- Exercise Specialist: Exercise physiology expert

All agents use Google's Gemini Pro model for AI processing.

Author: Blood Test Analyser Team
Version: 1.0.0
Last Updated: 2024
"""

## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

from tools import search_tool, BloodTestReportTool

### Loading LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

# Creating an Experienced Doctor agent
doctor=Agent(
    role="Senior Medical Doctor and Blood Test Analyst",
    goal="Provide accurate and comprehensive analysis of blood test reports for the query: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You are a highly experienced medical doctor with expertise in interpreting blood test reports. "
        "You have years of experience in clinical practice and are known for your thorough analysis. "
        "You always provide evidence-based medical advice and recommendations. "
        "You understand the importance of accurate diagnosis and patient safety."
    ),
    tools=[BloodTestReportTool()],
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=True  # Allow delegation to other specialists
)

# Creating a verifier agent
verifier = Agent(
    role="Medical Document Verifier",
    goal="Verify that uploaded documents are valid blood test reports and contain relevant medical data for the query: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You are a medical records specialist with expertise in document verification. "
        "You carefully examine uploaded files to ensure they are legitimate blood test reports. "
        "You understand medical terminology and can identify relevant health data. "
        "You prioritize accuracy and patient safety in your verification process."
    ),
    llm=llm,
    max_iter=2,
    max_rpm=5,
    allow_delegation=True
)


nutritionist = Agent(
    role="Clinical Nutritionist",
    goal="Provide evidence-based nutritional recommendations based on blood test results for the query: {query}",
    verbose=True,
    backstory=(
        "You are a certified clinical nutritionist with 15+ years of experience. "
        "You specialize in interpreting blood test results and providing personalized nutrition advice. "
        "You base your recommendations on scientific evidence and medical guidelines. "
        "You understand the relationship between blood markers and nutritional needs."
    ),
    llm=llm,
    max_iter=3,
    max_rpm=8,
    allow_delegation=False
)


exercise_specialist = Agent(
    role="Exercise Physiology Specialist",
    goal="Create safe and effective exercise plans based on blood test results for the query: {query}",
    verbose=True,
    backstory=(
        "You are an exercise physiologist with expertise in creating personalized fitness programs. "
        "You understand how blood test results can influence exercise recommendations. "
        "You prioritize safety and create programs suitable for individual health conditions. "
        "You have experience working with patients of various ages and health statuses."
    ),
    llm=llm,
    max_iter=3,
    max_rpm=8,
    allow_delegation=False
)
