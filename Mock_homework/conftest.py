import time
import requests
from requests.exceptions import ConnectionError
import settings


def wait_ready(host, port):
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


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):

        from mock import flask_mock
        flask_mock.run_mock()

        wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)


def pytest_unconfigure():
    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')
