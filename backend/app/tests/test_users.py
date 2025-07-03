import pytest 
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def user_payload():
    return {
        "username": "prueba-user", 
        "password": "user123", 
        "email": "user@gmail.com"
    }

@pytest.fixture
def created_user():
    response = client.post(url="/users/", json=user_payload)
    assert response.status_Code == 200
    return response.json()

def test_create_user():
    response = client.post(url="/users/", json=user_payload)
    assert response.status_Code == 200

    data_response = response.json()
    assert data_response.username == user_payload["username"]
    assert data_response.password == user_payload["password"]
    assert data_response.email == user_payload["email"]

def test_create_duplicate_user():
    response = client.post(url="/users/", json=user_payload)
    assert response.status_code == 400
    assert response.json() == {"detail": "You can't create a user again with the same username."}

def test_get_user_by_id(created_user):
    user_id = created_user["id"]
    response = client.get(url=f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()

    assert data["username"] == created_user["username"]
    assert data["email"] == created_user["email"]
