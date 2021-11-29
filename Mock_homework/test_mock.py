import settings
import json
from mock.flask_mock import SURNAME_DATA
from base import BaseCase
import requests
import pytest


@pytest.mark.mock
class TestMock(BaseCase):

    def test_get_mock(self, make_user):
        SURNAME_DATA[make_user['name']] = make_user['surname']
        response = self.mock_client.get(params=f"/get_surname/{make_user['name']}")
        assert json.loads(response[-1])['surname'] == make_user['surname']

    def test_post_mock(self, make_user):
        self.mock_client.post(params='/add_surname', data='{"name":'+make_user['name'] +
                                                     ' , "surname":'+make_user['surname']+'}')
        assert SURNAME_DATA[make_user['name']] == make_user['surname']

    def test_put_mock(self, make_user):
        requests.put(url=f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/change_surname',
        json={"name": make_user['name'], "surname": make_user['surname']})
        assert SURNAME_DATA[make_user['name']] == make_user['surname']

    def test_delete_mock(self, make_user):
        SURNAME_DATA[make_user['name']] = make_user['surname']
        self.mock_client.delete(params=f'/delete_surname/{make_user["name"]}')
        assert make_user['name'] not in SURNAME_DATA
