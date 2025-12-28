from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from dotenv import load_dotenv
from openai import OpenAI
from rag import ingest_pdf, query_pdf

# -----------------------------------
# Load environment variables
# -----------------------------------
load_dotenv()

# -----------------------------------
# App setup
# -----------------------------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------
# OpenAI Client
# -----------------------------------
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# -----------------------------------
# Upload PDF & index
# -----------------------------------
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    path = f"temp_{file.filename}"

    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    ingest_pdf(path)

    return {"message": "PDF uploaded and indexed successfully"}

# -----------------------------------
# Ask Question
# -----------------------------------
@app.post("/ask")
async def ask_question(question: str):
    context = query_pdf(question)

    prompt = f"""
You are a helpful assistant.
Answer the question using ONLY the context below.
If the answer is not present, say "Answer not found in the document."

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "answer": response.choices[0].message.content
    }
