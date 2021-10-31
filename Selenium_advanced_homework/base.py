import os

import allure
import pytest
from _pytest.fixtures import FixtureRequest
# from selenium.webdriver.remote.webdriver import WebDriver

from ui.pages.base_page import BasePage
from ui.pages.campaign_page import CampaignPage
from ui.fixtures import get_driver


class BaseCase:

    driver = None
    authorize = True
    authorize_fail = False

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_tests_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_tests_count:
            screenshot = os.path.join(temp_dir, 'failure.png')
            driver.get_screenshot_as_file(screenshot)
            allure.attach.file(screenshot, 'failure.png', attachment_type=allure.attachment_type.PNG)

            browser_log = os.path.join(temp_dir, 'browser.log')
            with open(browser_log, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")

            with open(browser_log, 'r') as f:
                allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)

    @pytest.fixture(scope='session')
    def cookies(self, config, credentials):
        driver = get_driver(config=config)
        driver.get(url=config['url'])
        driver.maximize_window()
        login_page = BasePage(driver=driver)
        login_page.login(*credentials)
        cookies = driver.get_cookies()
        driver.quit()

        return cookies

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config, logger, ui_report, temp_dir, enter):
        self.config = config
        self.logger = logger
        self.path = temp_dir
        self.campaign_page = enter

    @pytest.fixture(scope='function')
    def enter(self, driver, credentials, request: FixtureRequest):
        self.driver = driver
        self.login_page = BasePage(driver=self.driver)
        if self.authorize_fail:
            return None
        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)

            self.driver.refresh()

        else:
            self.login_page.login(*credentials)

        return CampaignPage(driver=self.driver)
