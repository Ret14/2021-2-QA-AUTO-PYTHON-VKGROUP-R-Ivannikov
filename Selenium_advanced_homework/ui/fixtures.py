import logging
import allure
import pytest
import numpy
from PIL import Image
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(config, download_dir=None):
    browser_name = config['browser']
    selenoid = config['selenoid']
    vnc = config['vnc']

    options = Options()
    if download_dir is not None:
        options.add_experimental_option("prefs", {"download.default_directory": download_dir})

    if selenoid:
        options.add_experimental_option("prefs", {"download.default_directory": '/home/selenium/Downloads'})
        capabilities = {
            'browserName': 'chrome',
            'version': '89.0'
        }
        if vnc:
            capabilities['version'] += '_vnc'
            capabilities['enableVNC'] = True

        browser = webdriver.Remote(selenoid, options=options,
                                       desired_capabilities=capabilities)
    else:
        manager = ChromeDriverManager(version='latest', log_level=logging.CRITICAL)
        browser = webdriver.Chrome(executable_path=manager.install(), options=options)

    return browser


@pytest.fixture(scope='function')
def driver(config, temp_dir):
    url = config['url']
    with allure.step('Init browser'):
        browser = get_driver(config, download_dir=temp_dir)
        browser.get(url)
    browser.maximize_window()
    yield browser
    browser.close()
    browser.quit()


@pytest.fixture(scope='session')
def credentials(path='C:\\tmp\\user\\credentials.txt'):
    with open(path, 'r') as f:
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
