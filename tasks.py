from main import run_crew
from models import SessionLocal, User, AnalysisResult

def process_analysis_job(query, file_path, file_name):
    response = run_crew(query=query, file_path=file_path)
    db = SessionLocal()
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
        file_processed=file_name
    )
    db.add(analysis_result)
    db.commit()
    db.refresh(analysis_result)
    db.close()
    return {
        "status": "success",
        "query": query,
        "analysis": str(response),
        "file_processed": file_name
    } 