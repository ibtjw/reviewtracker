import pytest
import json
from flask import testing
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_parse_reviews(client: testing.FlaskClient):
    response = client.post('/reviews', data = {'url': 'https://www.lendingtree.com/reviews/business/seek-capital/65175902'})

    reviews = json.loads(response.data)

    assert len(reviews) > 0
    
    for review in reviews:
        assert 'author' in review
        assert len(review['author']) > 0

        assert 'date' in review
        assert len(review['date']) > 0

        assert 'title' in review
        assert len(review['title']) > 0
        
        assert 'content' in review
        assert len(review['content']) > 0

        assert 'stars' in review
        assert len(review['stars']) > 0

        assert 'loan_type' in review
        assert len(review['loan_type']) > 0