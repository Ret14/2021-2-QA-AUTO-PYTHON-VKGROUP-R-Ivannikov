import os

import allure
import pytest
from ui.pages.main_page import MainPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, capabilities, test_dir):
        self.driver = driver
        self.main_page = MainPage(driver=self.driver)
        self.app_version = self.get_version(capabilities)
        self.path = test_dir

    @pytest.fixture(scope='function')
    def news_source_page(self, settings_page):
        return settings_page.go_to_news_source_page()

    @pytest.fixture(scope='function')
    def settings_page(self, main_page):
        return main_page.go_to_settings_page()

    @pytest.fixture(scope='function')
    def main_page(self):
        return self.main_page

    @pytest.fixture(scope='function')
    def search_page(self, main_page):
        return main_page.go_to_search_page()

    @pytest.fixture(scope='function')
    def about_app_page(self, settings_page):
        return settings_page.go_to_about_app_page()

    @staticmethod
    def get_version(caps: dict):
        return caps['app'].split('/')[-1].split('_v')[-1].split('.apk')[0]

    def make_a_shot(self, name=None):
        name = name + '.png'
        screenshot = os.path.join(self.path, name)
        self.driver.get_screenshot_as_file(screenshot)
        allure.attach.file(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
