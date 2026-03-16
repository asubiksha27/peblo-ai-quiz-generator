# Peblo AI Quiz Generator

This project is an AI-powered quiz generator that creates quiz questions from uploaded PDF documents.

## Features

* Upload a PDF document
* Extract text from the PDF
* Generate quiz questions automatically
* Retrieve quiz questions through API
* Submit answers and get evaluation

## Tech Stack

* Python
* FastAPI
* Uvicorn
* PyMuPDF
* SQLite

## API Endpoints

### Upload PDF

POST /ingest

### Generate Quiz

POST /generate-quiz

### Get Quiz

GET /quiz

### Submit Answer

POST /submit-answer

## How to Run the Project

Clone the repository:

git clone https://github.com/asubiksha27/peblo-ai-quiz-generator.git

Go to the project folder:

cd peblo-ai-quiz-generator

Create virtual environment:

python -m venv venv

Activate environment:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the server:

uvicorn app.main:app --reload

Open API documentation in browser:

http://127.0.0.1:8000/docs


## Architecture

PDF Upload (POST /ingest)
     ↓
Text Extraction (app/pdf_ingest.py)
     ↓
Content Chunking
     ↓
LLM Quiz Generation (app/quiz_generator.py)
     ↓
SQLite Database (app/models.py / app/database.py)
     ↓
FastAPI Endpoints (app/main.py)
