from fastapi import FastAPI, UploadFile, File
from sqlalchemy.orm import Session
import shutil

from .database import engine, SessionLocal
from .models import Base, Question
from .pdf_ingest import extract_text_from_pdf
from .quiz_generator import generate_questions

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/ingest")
async def ingest_pdf(file: UploadFile = File(...)):

    path = f"temp_{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(path)

    return {"message": "PDF processed", "length": len(text)}


@app.post("/generate-quiz")
def generate_quiz():

    text = "triangle has three sides"

    questions = generate_questions(text)

    db: Session = SessionLocal()

    for q in questions:
        question = Question(
            question=q["question"],
            options=q["options"],
            answer=q["answer"],
            difficulty=q["difficulty"]
        )

        db.add(question)

    db.commit()

    return {"message": "Quiz generated"}


@app.get("/quiz")
def get_quiz():

    db: Session = SessionLocal()

    questions = db.query(Question).all()

    return questions


@app.post("/submit-answer")
def submit_answer(question_id: int, selected_answer: str):

    db: Session = SessionLocal()

    question = db.query(Question).filter(Question.id == question_id).first()

    correct = question.answer == selected_answer

    return {
        "correct": correct,
        "correct_answer": question.answer
    }