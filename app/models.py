from sqlalchemy import Column, Integer, String, Text
from .database import Base

class ContentChunk(Base):
    __tablename__ = "content_chunks"

    id = Column(Integer, primary_key=True)
    source_id = Column(String)
    topic = Column(String)
    text = Column(Text)


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(Text)
    options = Column(Text)
    answer = Column(String)
    difficulty = Column(String)
    source_chunk_id = Column(Integer)


class StudentAnswer(Base):
    __tablename__ = "student_answers"

    id = Column(Integer, primary_key=True)
    student_id = Column(String)
    question_id = Column(Integer)
    selected_answer = Column(String)