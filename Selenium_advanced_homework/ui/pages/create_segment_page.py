import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from utils.decorators import wait


class CreateSegmentPage(BasePage):

    locators = basic_locators.CreateSegmentPageLocators

    @allure.step('Creating a segment')
    def create_new_segment(self, audience_page):
        self.click(self.locators.SEGMENT_TYPE_TAB)
        self.click(self.locators.SEGMENT_TYPE_CHECKBOX)
        self.click(self.locators.ADD_SEGMENT_BTN)
        content = self.generate_string()
        self.fill_up(self.locators.SEGMENT_NAME_INPUT, content)
        self.click(self.locators.CREATE_SEGMENT_BTN)
        self.logger.info(f'Segment "{content}" is created')
        wait(method=self.elements_find, locator=self.format_locator(self.locators.SEARCH_BY_TEXT, content))
        with allure.step('Giving the segment name to audience_page'):
            audience_page.segment_name = content
        return audience_page
