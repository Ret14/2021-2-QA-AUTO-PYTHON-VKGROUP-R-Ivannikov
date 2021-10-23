import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome(executable_path='D:/mailAutotest/Webdrivers/chromedriver.exe')
    driver.maximize_window()
    driver.get('https://target.my.com/')
    yield driver
    driver.close()
    driver.quit()
