import pytest 
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture(scope="session")
def user_payload():
    return {
        "username": "prueba-user", 
        "password": "user123", 
        "email": "user@gmail.com"
    }

@pytest.fixture(scope="module")
def test_created_user(user_payload):
    response = client.post(url="/users/", json=user_payload)
    assert response.status_code == 200
    data_response = response.json()
    assert data_response["username"] == user_payload["username"]
    assert data_response["password"] == user_payload["password"]
    assert data_response["email"] == user_payload["email"]

    return data_response


def test_get_user_by_id(test_created_user):
    user_id = test_created_user["id"]
    response = client.get(url=f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()

    assert data["username"] == test_created_user["username"]
    assert data["email"] == test_created_user["email"]
    
def test_create_duplicate_user(user_payload):
    response = client.post(url="/users/", json=user_payload)
    assert response.status_code == 400
    assert response.json() == {"detail": "You can't create a user again with the same username."}

def test_post_password(test_created_user):
    user_id = test_created_user["id"]
    response = client.put(url=f"/users/{user_id}", json={"password": "nuevo1user"})
    assert response.status_code == 200
    data_res = response.json()
    assert data_res["password"] == "nuevo1user"

def test_delete_user_by_username(user_payload):
    username_target = user_payload["username"]
    print(f"username_target: {username_target}")
    response = client.delete(url=f"/users/{username_target}")
    assert response.status_code == 200
    assert response.json() == {"message": f"User {username_target} removed succesfully!"}