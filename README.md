# 🧠 AI Summarizer API

An end-to-end **RESTful API** built with **FastAPI** that uses **Transformer-based models (BART)** to summarize documents or text.

## 🚀 Features
- Summarize text or uploaded documents (PDF, DOCX, TXT)
- Built with **FastAPI** following REST best practices
- Uses **Hugging Face Transformers**
- Dockerized for easy deployment

## 🧪 Run Locally
```bash
git clone https://github.com/YOUR-USERNAME/ai_summarizer_api.git
cd ai_summarizer_api
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Then open: http://127.0.0.1:8000/docs

## 📦 API Endpoints
- `POST /summarize` → Summarize text input
- `POST /upload` → Upload file (PDF/DOCX/TXT) and get summary

## 🧠 Example
```json
{
  "summary": "FastAPI enables rapid and efficient API development using Python."
}
```
