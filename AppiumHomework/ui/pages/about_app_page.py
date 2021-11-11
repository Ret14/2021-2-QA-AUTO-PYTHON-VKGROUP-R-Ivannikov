from ui.locators.app_locators import BaseLocators
from ui.pages.base_page import BasePage


class AboutAppPage(BasePage):

    locators = BaseLocators()

    def version_and_trademark_assertions(self, version=None):
        assert self.text_search(version)
        assert self.text_search('права защищены')
