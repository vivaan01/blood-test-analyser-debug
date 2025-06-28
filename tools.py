"""
Blood Test Report Analyser - Custom Tools
========================================

This module defines custom tools used by AI agents for processing blood test reports.
These tools handle PDF file reading, data processing, and specialized analysis functions.

Tools:
- BloodTestReportTool: PDF reading and data extraction
- NutritionTool: Nutritional analysis (placeholder for future implementation)
- ExerciseTool: Exercise planning (placeholder for future implementation)
- search_tool: Web search functionality using Serper API

All tools are designed to work with the CrewAI framework and provide
reliable data processing capabilities.

Author: Blood Test Analyser Team
Version: 1.0.0
Last Updated: 2024
"""

## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import tools
from crewai_tools import SerperDevTool
from langchain_community.document_loaders import PyPDFLoader
from crewai_tools import RagTool

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
class BloodTestReportTool(RagTool):
    name: str = "BloodTestReportReader"
    description: str = "Reads and extracts text from a blood test PDF report."

    def _run(self, path='data/sample.pdf'):
        docs = PyPDFLoader(file_path=path).load()
        full_report = ""
        for data in docs:
            content = data.page_content
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"
        return full_report

## Creating Nutrition Analysis Tool
class NutritionTool:
    def analyze_nutrition_tool(self, blood_report_data):
        # Process and analyze the blood report data
        processed_data = blood_report_data
        
        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
                
        # TODO: Implement nutrition analysis logic here
        return "Nutrition analysis functionality to be implemented"

## Creating Exercise Planning Tool
class ExerciseTool:
    def create_exercise_plan_tool(self, blood_report_data):        
        # TODO: Implement exercise planning logic here
        return "Exercise planning functionality to be implemented"

def blood_test_report_reader(path='data/sample.pdf'):
    docs = PyPDFLoader(file_path=path).load()
    full_report = ""
    for data in docs:
        content = data.page_content
        while "\n\n" in content:
            content = content.replace("\n\n", "\n")
        full_report += content + "\n"
    return full_report