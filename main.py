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

import os
import uuid
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import doctor, verifier, nutritionist, exercise_specialist
from task import help_patients
from tools import BloodTestReportTool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, AnalysisResult

load_dotenv()

app = FastAPI(title="Blood Test Report Analyser", version="1.0.0")

# Database setup
DATABASE_URL = "sqlite:///./blood_test_analyser.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

def run_crew(query: str, file_path: str):
    """Run the medical crew for blood test analysis"""
    try:
        # Create crew with all agents
        medical_crew = Crew(
            agents=[doctor, verifier, nutritionist, exercise_specialist],
            tasks=[help_patients],
            process=Process.sequential,
        )
        
        result = medical_crew.kickoff({
            'query': query,
            'file_path': file_path
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.get("/")
async def health_check():
    """Health check endpoint"""
    return {"message": "Blood Test Report Analyser API is running"}

@app.post("/analyze")
async def analyze_blood_report(
    file: UploadFile = File(...),
    query: str = Form(default="Summarise my Blood Test Report")
):
    """Analyze blood test report from uploaded PDF"""
    
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    if query == "" or query is None:
        query = "Summarise my Blood Test Report"
    
    file_id = str(uuid.uuid4())
    file_path = f"data/blood_test_report_{file_id}.pdf"
    
    try:
        # Create data directory if it doesn't exist
        os.makedirs("data", exist_ok=True)
        
        # Save uploaded file
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Run analysis
        response = run_crew(query=query.strip(), file_path=file_path)
        
        # Save to database
        db = SessionLocal()
        try:
            user = db.query(User).filter_by(email="demo@user.com").first()
            if not user:
                user = User(username="demo", email="demo@user.com")
                db.add(user)
                db.commit()
                db.refresh(user)
            
            analysis_result = AnalysisResult(
                user_id=user.id,
                query=query,
                analysis=str(response),
                file_processed=file.filename
            )
            db.add(analysis_result)
            db.commit()
            db.refresh(analysis_result)
        finally:
            db.close()
        
        # Clean up file
        if os.path.exists(file_path):
            os.remove(file_path)
        
        return JSONResponse(content={
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        })
        
    except Exception as e:
        # Clean up file on error
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)