"""
Blood Test Report Analyser - Main Application
============================================

This is the main FastAPI application for analyzing blood test reports using AI.
The application provides a REST API that allows users to upload PDF blood test reports
and receive comprehensive AI-powered analysis and health recommendations.

Features:
- PDF blood test report upload and processing
- AI-powered medical analysis using CrewAI framework
- Comprehensive health recommendations
- File cleanup and error handling

Author: Blood Test Analyser Team
Version: 1.0.0
Last Updated: 2024
"""

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
import asyncio

from crewai import Crew, Process
from agents import doctor
from task import help_patients

app = FastAPI(title="Blood Test Report Analyser")

def run_crew(query: str, file_path: str="data/sample.pdf"):
    """To run the whole crew"""
    medical_crew = Crew(
        agents=[doctor],
        tasks=[help_patients],
        process=Process.sequential,
    )
    
    result = medical_crew.kickoff({
        'query': query,
        'file_path': file_path
    })
    return result

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Blood Test Report Analyser API is running"}

@app.post("/analyze")
async def analyze_blood_report(
    file: UploadFile = File(...),
    query: str = Form(default="Summarise my Blood Test Report")
):
    """Analyze blood test report and provide comprehensive health recommendations"""
    
    # Generate unique filename to avoid conflicts
    file_id = str(uuid.uuid4())
    file_path = f"data/blood_test_report_{file_id}.pdf"
    
    try:
        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)
        
        # Save uploaded file
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Validate query
        if query == "" or query is None:
            query = "Summarise my Blood Test Report"
            
        # Process the blood report with all specialists
        response = run_crew(query=query.strip(), file_path=file_path)
        
        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing blood report: {str(e)}")
    
    finally:
        # Clean up uploaded file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass  # Ignore cleanup errors

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)