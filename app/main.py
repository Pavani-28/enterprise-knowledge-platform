from fastapi import FastAPI  #imports framework
from app.schemas import QuestionRequest

app = FastAPI(                              #app=FASTAPI()....this craetes our application instance
    title="Enterprise Knowledge Intelligence Platform",
    description="An enterprise RAG-based document intelligence system",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Enterprise Knowledge Intelligence Platform API is running"
    }

@app.post("/questions")
def ask_question(request: QuestionRequest):
    return {
        "received_question": request.question
    }