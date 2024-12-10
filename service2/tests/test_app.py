import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_reviews(client):
    rv = client.get('/reviews')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['reviews'][0]['review'] == 'Great Book!'
