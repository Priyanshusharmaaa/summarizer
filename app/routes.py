from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from app.summarizer import summarize_text
from app.utils import extract_text_from_file

router = APIRouter()

class SummarizeRequest(BaseModel):
    text: str

@router.post("/summarize", tags=["Summarization"])
async def summarize(req: SummarizeRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")
    summary = summarize_text(req.text)
    return {"summary": summary}

@router.post("/upload", tags=["Summarization"])
async def upload_file(file: UploadFile = File(...)):
    text = await extract_text_from_file(file)
    if not text.strip():
        raise HTTPException(status_code=400, detail="Uploaded file contains no readable text.")
    summary = summarize_text(text)
    return {"filename": file.filename, "summary": summary}