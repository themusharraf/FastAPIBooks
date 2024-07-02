from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_users():
    requests = client.get("/users/")
    assert requests.status_code == 200
    assert requests.json()[0] == {'books': [{'id': 1,
                                             'isbn': '12-vbr5',
                                             'language': 'English',
                                             'pages': 1400,
                                             'title': 'Python cook book',
                                             'user_id': 1,
                                             'year': '2024-06-25T13:32:52.703384'}],
                                  'email': 'user@example.com',
                                  'id': 1,
                                  'is_active': True,
                                  'username': 'string'}


def test_get_books():
    requests = client.get("/books/")
    assert requests.status_code == 200
    assert requests.json()[0] == {'id': 1,
                                  'isbn': '12-vbr5',
                                  'language': 'English',
                                  'pages': 1400,
                                  'title': 'Python cook book',
                                  'user_id': 1,
                                  'year': '2024-06-25T13:32:52.703384'}


def test_get_book():
    requests = client.get("/books/1")
    assert requests.status_code == 200
    assert requests.json() == {'id': 1,
                               'isbn': '12-vbr5',
                               'language': 'English',
                               'pages': 1400,
                               'title': 'Python cook book',
                               'user_id': 1,
                               'year': '2024-06-25T13:32:52.703384'}


def test_get_user():
    requests = client.get("/users/1")
    assert requests.status_code == 200
    assert requests.json()['email'] == 'user@example.com'
    assert requests.json()['is_active'] == True
    assert requests.json()['id'] == 1
