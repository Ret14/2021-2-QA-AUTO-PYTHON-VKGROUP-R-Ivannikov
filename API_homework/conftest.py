import logging
import os
import shutil
import sys
import numpy
from PIL import Image
import pytest
from api.client import ApiClient
import allure


def pytest_addoption(parser):
    parser.addoption('--debug_log', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    debug_log = request.config.getoption('--debug_log')

    return {'debug_log': debug_log}


@pytest.fixture(scope='function')
def logger(temp_dir, config):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    log_file = os.path.join(temp_dir, 'test.log')
    log_level = logging.DEBUG if config['debug_log'] else logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()

    with open(log_file, 'r') as f:
        allure.attach(f.read(), 'test.log', attachment_type=allure.attachment_type.TEXT)


def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tmp\\tests'
    else:
        base_dir = '/tmp/tests'

    if not hasattr(config, 'workerinput'):  # in master only
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)

        os.makedirs(base_dir)

    config.base_temp_dir = base_dir  # everywhere


@pytest.fixture(scope='function')
def temp_dir(request):
    test_dir = os.path.join(request.config.base_temp_dir,
                            request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_'))
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope='session')
def credentials(repo_root, cred_name='credentials.txt'):
    cred_path = os.path.join(repo_root, cred_name)
    with open(cred_path, 'r') as f:
        user = f.readline().strip()
        password = f.readline().strip()

    return user, password


@pytest.fixture(scope='session')
def api_client(credentials):
    return ApiClient(*credentials)


@pytest.fixture(scope='function')
def prepare_image(temp_dir):
    pic_array = numpy.random.rand(400, 240, 3) * 255
    pic_240 = Image.fromarray(pic_array.astype('uint8')).convert('L')
    path_240 = os.path.join(temp_dir, '240x400.png')
    pic_240.save(path_240)
    return path_240
