"""
Blood Test Report Analyser - Task Definitions
============================================

This module defines the tasks that AI agents perform in the blood test analysis system.
Each task has a specific purpose and expected output format for consistent results.

Tasks:
- help_patients: Main blood test analysis task
- nutrition_analysis: Nutritional recommendations based on blood results
- exercise_planning: Exercise recommendations based on health status
- verification: Document verification and validation

All tasks are designed to work with PDF blood test reports and provide
evidence-based medical recommendations.

Author: Blood Test Analyser Team
Version: 1.0.0
Last Updated: 2024
"""

## Importing libraries and files
from crewai import Task

from agents import doctor, verifier
from tools import search_tool, BloodTestReportTool

## Creating a task to help solve user's query
help_patients = Task(
    description="Analyze the blood test report at {file_path} and provide comprehensive analysis for the user's query: {query}. "
                "Read the PDF file carefully and provide accurate medical insights. "
                "Identify any abnormalities in the blood test results and provide evidence-based recommendations. "
                "Search for relevant medical information if needed to support your analysis.",

    expected_output="""Provide a comprehensive blood test analysis including:
- Summary of key findings from the blood test report
- Identification of any abnormal values with explanations
- Evidence-based health recommendations
- Lifestyle and dietary suggestions based on the results
- When to consult a healthcare provider
- Any follow-up tests that might be recommended""",

    agent=doctor,
    tools=[BloodTestReportTool()],
    async_execution=False,
)

## Creating a nutrition analysis task
nutrition_analysis = Task(
    description="Analyze the blood test report at {file_path} and provide evidence-based nutritional recommendations for the query: {query}. "
                "Focus on blood markers that relate to nutrition such as glucose, cholesterol, vitamins, and minerals. "
                "Provide personalized dietary advice based on the test results.",

    expected_output="""Provide comprehensive nutritional analysis including:
- Key nutritional markers from the blood test
- Evidence-based dietary recommendations
- Foods to include or avoid based on results
- Supplement recommendations if medically indicated
- Lifestyle modifications for better nutrition
- When to consult a registered dietitian""",

    agent=doctor,
    tools=[BloodTestReportTool()],
    async_execution=False,
)

## Creating an exercise planning task
exercise_planning = Task(
    description="Create a safe and effective exercise plan based on the blood test report at {file_path} for the query: {query}. "
                "Consider any health conditions indicated by the blood test results. "
                "Provide personalized exercise recommendations that are appropriate for the individual's health status.",

    expected_output="""Create a comprehensive exercise plan including:
- Safe exercise recommendations based on blood test results
- Intensity and frequency guidelines
- Exercise modifications for any health conditions
- Cardiovascular and strength training suggestions
- Safety precautions and warning signs
- Gradual progression recommendations""",

    agent=doctor,
    tools=[BloodTestReportTool()],
    async_execution=False,
)

    
verification = Task(
    description="Verify that the document at {file_path} is a valid blood test report and contains relevant medical data for the query: {query}. "
                "Check for proper medical terminology and blood test parameters.",

    expected_output="""Provide verification results including:
- Confirmation of document type (blood test report)
- Identification of key blood test parameters
- Assessment of report completeness
- Any concerns about document validity
- Recommendations for additional information if needed""",

    agent=doctor,
    tools=[BloodTestReportTool()],
    async_execution=False
)