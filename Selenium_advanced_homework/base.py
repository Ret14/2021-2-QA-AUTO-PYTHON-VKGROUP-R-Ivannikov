import os
import allure
import pytest
from ui.pages.login_page import LoginPage
from ui.pages.campaign_page import CampaignPage


class BaseCase:

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

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, ui_report, temp_dir):
        self.config = config
        self.driver = driver
        self.logger = logger
        self.path = temp_dir
        self.login_page = LoginPage(driver=self.driver)

    @pytest.fixture(scope='function')
    def login(self, credentials):
        if self.login_page.login(*credentials).startswith('https://target.my.com/dashboard'):
            return CampaignPage(driver=self.driver)

    @pytest.fixture(scope='function')
    def create_segment_page(self, audience_page):
        return audience_page.create_segment()

    @pytest.fixture(scope='function')
    def audience_page(self, campaign_page):
        return campaign_page.go_to_audience_page()

    @pytest.fixture(scope='function')
    def create_campaign_page(self, campaign_page):
        return campaign_page.create_campaign()

    @pytest.fixture(scope='function')
    def campaign_page(self, login):
        return login

    def make_a_shot(self, name=None):
        name = name + '.png'
        screenshot = os.path.join(self.path, name)
        self.driver.get_screenshot_as_file(screenshot)
        allure.attach.file(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
