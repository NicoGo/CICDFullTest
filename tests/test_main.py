from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_hello():
    """New function another change..."""
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, I was world now with some new return !"}
