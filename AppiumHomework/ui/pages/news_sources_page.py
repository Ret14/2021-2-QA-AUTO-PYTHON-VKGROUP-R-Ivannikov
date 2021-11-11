import allure
from ui.locators.app_locators import NewsSourcesPageLocators
from ui.pages.base_page import BasePage
from utils.decorators import wait


class NewsSourcesPage(BasePage):

    locators = NewsSourcesPageLocators()

    def choose_news_fm(self):
        self.click(self.locators.NEWS_FM_TAB)
        wait(method=self.elements_find, locator=self.locators.CHECK_ELEM)
        assert self.elements_find(self.locators.CHECK_ELEM), 'Check is not found!'

    @allure.step('Returning to MainPage')
    def back_to_main_page(self):
        self.driver.back()
        self.driver.back()

