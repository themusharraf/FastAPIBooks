from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_users():
    requests = client.get("/users/")
    assert requests.status_code == 200
    assert type(requests.json()) == list


def test_get_books():
    requests = client.get("/books/")
    assert requests.status_code == 200
    assert type(requests.json()) == list


def test_get_book():
    requests = client.get("/books/1")
    assert requests.status_code == 200
    assert type(requests.json()) == dict


def test_get_user():
    requests = client.get("/users/1")
    assert requests.status_code == 200
    assert type(requests.json()['email']) == str
    assert type(requests.json()['is_active']) == bool
