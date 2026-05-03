from fastapi import FastAPI
from pydantic import BaseModel
import ollama

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str
@app.post("/ask")
def ask(q: Question):

    user_question = q.question.lower()

    # Custom hardcoded responses
    if "who made you" in user_question:
        return {
            "answer": "I was created by Rohit Yadav."
        }

    if "who created you" in user_question:
        return {
            "answer": "I was created by Rohit Yadav."
        }

    if "owner" in user_question:
        return {
            "answer": "I was created by Rohit Yadav."
        }

    response = ollama.chat(
        model='phi3',
        messages=[
            {
                "role": "system",
                "content": """
You are Titan AI created by Rohit Yadav.
Never mention OpenAI or Microsoft.
"""
            },
            {
                "role": "user",
                "content": q.question
            }
        ]
    )

    return {
        "answer": response['message']['content']
    } 