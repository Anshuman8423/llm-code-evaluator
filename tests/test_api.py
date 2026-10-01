from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "LLM Code Evaluator API is running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_empty_code():
    response = client.post(
        "/evaluate",
        json={
            "code": "",
            "language": "python",
            "problem": "Write an addition function"
        }
    )

    assert response.status_code == 400


def test_empty_problem():
    response = client.post(
        "/evaluate",
        json={
            "code": "print('Hello')",
            "language": "python",
            "problem": ""
        }
    )

    assert response.status_code == 400