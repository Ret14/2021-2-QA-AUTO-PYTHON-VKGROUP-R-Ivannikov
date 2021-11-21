import allure
from ui.locators.app_locators import SearchPageLocators
from ui.pages.base_page import BasePage
from utils.decorators import wait


class SearchPage(BasePage):

    locators = SearchPageLocators()

    @allure.step('Searching "{query}"')
    def make_query(self, query=None):
        self.find(self.locators.QUERY_INPUT).send_keys(query)
        self.click(self.locators.SEND_BTN)

    def first_query_wait(self):
        wait(method=self.elements_find, locator=self.locators.THUMB_UP_TAB)

    def type_text_and_swipe(self):
        self.make_query('Russia')
        self.first_query_wait()
        self.swipe_element_left(locator=self.locators.THUMB_UP_TAB)
        self.click(self.locators.POPULATION_TAB)
        self.query_wait()

    def query_wait(self):
        wait(method=self.not_on_page, locator=self.locators.THUMB_UP_TAB)
        wait(method=self.elements_find, locator=self.locators.THUMB_UP_TAB)

    def do_the_math(self):
        self.make_query('2**10')
        self.first_query_wait()

    def type_news(self):
        self.make_query('News')
        self.first_query_wait()
