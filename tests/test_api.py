from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_summarize_endpoint():
    response = client.post("/summarize", json={"text": "FastAPI is a modern Python web framework used to build APIs quickly."})
    assert response.status_code == 200
    assert "summary" in response.json()