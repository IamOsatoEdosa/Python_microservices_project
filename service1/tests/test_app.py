import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_books(client, mocker):
    mock_response = mocker.patch('app.requests.get')
    mock_response.return_value.json.return_value = {'reviews': [{'book_id': 1, 'review': 'Great Book!'}]}
    rv = client.get('/books')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['books'][0]['title'] == 'Book One'
    assert 'reviews' in json_data['books'][0]
