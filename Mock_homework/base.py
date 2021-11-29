import time
import pytest
import requests
from requests.exceptions import ConnectionError
from faker import Faker
from http_client.client import HttpClient
import settings

fake = Faker()


class BaseCase:

    def wait_ready(self, host, port):
        started = False
        st = time.time()
        while time.time() - st <= 5:
            try:
                requests.get(f'http://{host}:{port}')
                started = True
                break
            except ConnectionError:
                pass

        if not started:
            raise RuntimeError(f'{host}:{port} did not started in 5s!')

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        from mock import flask_mock
        flask_mock.run_mock()

        self.wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)
        self.mock_client = HttpClient(host=settings.MOCK_HOST, port=settings.MOCK_PORT)
        yield
        requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')

    @pytest.fixture(scope='function')
    def make_user(self):
        return {'name': fake.first_name, 'surname': fake.last_name}
