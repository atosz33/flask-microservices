import pytest
from app import app
from flask import json
import pytest_mongodb
from config import TestConfig

app, mongo = app.get_app_with_config(TestConfig)


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_index_page(client):
    """Start with a blank database."""
    rv = client.get('/')
    json_response = json.loads(rv.data)
    assert 'success' == json_response['result']


def test_add_order(client):
    rv = client.post(
            '/order',
            json={
                'product_id':1,
                'product_name':'test',
                'user_id' : 1,
                'price' : 3,
                'shipping_address': 'titkos',
                'quantity': 1,
                'shipped' : True,
                'arrived': True,
                })

    assert 201  ==  rv.status_code
