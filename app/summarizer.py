from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str) -> str:
    text = text.strip()
    if len(text) < 30:
        return "Text too short to summarize."
    result = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return result[0]["summary_text"]