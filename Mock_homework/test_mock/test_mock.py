import json
from mock.flask_mock import SURNAME_DATA
from base import BaseCase
import requests
import pytest


@pytest.mark.mock
class TestMock(BaseCase):

    def test_get_mock(self, user):
        SURNAME_DATA[user['name']] = user['surname']
        response = requests.get(url=f'{self.host}/get_surname/{user["name"]}')
        assert json.loads(response.text)['surname'] == user['surname']

    def test_get_mock_negative(self, user):
        response = requests.get(url=f'{self.host}/get_surname/{user["name"]}')
        assert response.status_code == 400

    def test_post_mock(self, user):
        headers = {
            'Content-Type': 'application/json'
        }
        requests.post(url=f'{self.host}/add_surname', headers=headers,
                      data=json.dumps({'name': user['name'], 'surname': user['surname']}))
        assert SURNAME_DATA[user['name']] == user['surname']

    def test_post_mock_negative(self, user):
        headers = {
            'Content-Type': 'application/json'
        }
        SURNAME_DATA[user['name']] = user['surname']
        response = requests.post(url=f'{self.host}/add_surname', headers=headers,
                                 data=json.dumps({'name': user['name'], 'surname': user['surname']}))

        assert response.status_code == 400

    def test_put_mock(self, user):
        SURNAME_DATA[user['name']] = user['surname']
        new_surname = self.fake.last_name()
        headers = {
            'Content-Type': 'application/json'
        }
        requests.put(url=f'{self.host}/change_surname', headers=headers,
                     data=json.dumps({'name': user['name'], 'surname': new_surname}))
        assert SURNAME_DATA[user['name']] == new_surname

    def test_put_mock_negative(self, user):
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.put(url=f'{self.host}/change_surname', headers=headers,
                                data=json.dumps({'name': user['name'], 'surname': user['surname']}))
        assert response.status_code == 400

    def test_delete_mock(self, user):
        SURNAME_DATA[user['name']] = user['surname']
        requests.delete(url=f'{self.host}/delete_surname/{user["name"]}')
        assert user['name'] not in SURNAME_DATA

    def test_delete_mock_negative(self, user):
        response = requests.delete(url=f'{self.host}/delete_surname/{user["name"]}')
        assert response.status_code == 400
