from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agent import ask_agent


app = FastAPI()


# Allow your React portfolio to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "Dhruv AI Agent is running"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    answer = ask_agent(request.message)

    return {
        "response": answer
    }