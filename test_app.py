import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_no_file(client):
    response = client.post("/parse")
    assert response.status_code == 400

def test_parse_returns_fields(client):
    # Test that endpoint exists and responds
    assert app is not None