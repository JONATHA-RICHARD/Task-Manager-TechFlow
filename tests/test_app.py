import pytest
from src.app import app

@pytest.fixture
def client():
    return app.test_client()

def test_create_and_get_task(client):
    response = client.post('/tasks', json={"title": "Teste", "description": "desc"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Teste"

    response2 = client.get('/tasks')
    assert response2.status_code == 200
    assert len(response2.get_json()) == 1

