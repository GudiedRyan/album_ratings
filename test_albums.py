import pytest
from app import app

def test_get_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

def test_get_create():
    with app.test_client() as client:
        response = client.get('/create')
        assert response.status_code == 200