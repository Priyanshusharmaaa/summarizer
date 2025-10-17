from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="AI Summarizer API",
    description="REST API that summarizes long documents using transformer models.",
    version="1.0.0",
)

app.include_router(router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the AI Summarizer API 🚀"}