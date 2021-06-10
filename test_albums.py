import pytest
from app import app
from app import create_app
from album_ratings.models import AlbumModel


# Routes
def test_get_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

def test_get_create():
    with app.test_client() as client:
        response = client.get('/create')
        assert response.status_code == 200

def test_404():
    with app.test_client() as client:
        response = client.get('/update/1')
        assert response.status_code == 404


# Test model

def test_new_album():
    album = AlbumModel(name='test', artist='Anon Y Mous', release_year=2013, rating=4)
    assert album.name == 'test'
    assert album.artist == 'Anon Y Mous'
    assert album.release_year == 2013
    assert album.rating == 4

