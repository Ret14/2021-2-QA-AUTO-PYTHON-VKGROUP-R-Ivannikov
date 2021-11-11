import os.path
import allure
import pytest
from appium import webdriver


@pytest.fixture(scope='session')
def capabilities(repo_root):
    with allure.step('Launching appium session with following capabilities'):
        capability = {"platformName": "Android",
                      "platformVersion": "8.1",
                      "automationName": "Appium",
                      "appPackage": "ru.mail.search.electroscope",
                      "appActivity": ".ui.activity.AssistantActivity",
                      "app": os.path.join(repo_root, 'apk/Marussia_v1.50.2.apk'),
                      "orientation": "PORTRAIT",
                      "autoGrantPermissions": "true",
                      }

    return capability


@pytest.fixture(scope='function')
def driver(config, capabilities):
    appium_url = config['appium']
    browser = webdriver.Remote(appium_url, desired_capabilities=capabilities)
    yield browser
    browser.quit()
