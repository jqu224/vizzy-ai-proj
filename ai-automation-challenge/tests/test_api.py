from fastapi.testclient import TestClient

from main import app


def test_health_endpoint():
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_moderate_endpoint_returns_structured_response():
    payload = {
        "content": "Check out my kitchen recipe where I chop vegetables safely.",
        "creator_id": "chef-123",
        "video_id": "video-123",
    }

    with TestClient(app) as client:
        response = client.post("/moderate", json=payload)

    body = response.json()
    assert response.status_code == 200
    assert body["video_id"] == "video-123"
    assert body["moderation"]["decision"] == "allow"
    assert body["moderation"]["provider"] == "openai+anthropic"
    assert "reasoning" in body["moderation"]
    assert "processing_time_ms" in body


def test_moderate_endpoint_rejects_empty_content():
    payload = {
        "content": "",
        "creator_id": "creator-123",
    }

    with TestClient(app) as client:
        response = client.post("/moderate", json=payload)

    assert response.status_code == 422
