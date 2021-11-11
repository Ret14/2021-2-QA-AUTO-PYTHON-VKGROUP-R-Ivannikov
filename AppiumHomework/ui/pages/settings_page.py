import allure
from ui.locators.app_locators import SettingsPageLocators
from ui.pages.about_app_page import AboutAppPage
from ui.pages.base_page import BasePage
from ui.pages.news_sources_page import NewsSourcesPage


class SettingsPage(BasePage):

    locators = SettingsPageLocators()

    def go_to_news_source_page(self):
        self.swipe_up()
        self.click(self.locators.NEWS_SOURCE_TAB)
        return NewsSourcesPage(driver=self.driver)

    def go_to_about_app_page(self):
        self.swipe_up_until_find_elem(locator=self.locators.ABOUT_APP_TAB)
        self.click(self.locators.ABOUT_APP_TAB)
        return AboutAppPage(driver=self.driver)
