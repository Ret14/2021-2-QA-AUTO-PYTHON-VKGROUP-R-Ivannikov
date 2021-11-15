import logging
import allure
import pytest
import numpy
from PIL import Image
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    manager = ChromeDriverManager(version='latest', log_level=logging.CRITICAL)
    service = Service(executable_path=manager.install())
    browser = webdriver.Chrome(service=service)
    return browser


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    with allure.step('Init browser'):
        browser = get_driver()
        browser.get(url)
    browser.maximize_window()
    yield browser
    browser.close()
    browser.quit()


@pytest.fixture(scope='session')
def credentials(repo_root, file_name='credentials.txt'):
    cred_path = os.path.join(repo_root, file_name)
    with open(cred_path, 'r') as f:
        user = f.readline().strip()
        password = f.readline().strip()

    return user, password


@pytest.fixture(scope='function')
def prepare_images(temp_dir):
    pic_array = numpy.random.rand(256, 256, 3) * 255
    pic_256 = Image.fromarray(pic_array.astype('uint8')).convert('L')
    path_256 = os.path.join(temp_dir, '256x256.png')
    pic_256.save(path_256)
    pic_array = numpy.random.rand(600, 600, 3) * 255
    pic_600 = Image.fromarray(pic_array.astype('uint8')).convert('L')
    path_600 = os.path.join(temp_dir, '600x600.png')
    pic_600.save(path_600)
    return {256: path_256, 600: path_600}
