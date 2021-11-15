import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.create_segment_page import CreateSegmentPage
from utils.decorators import wait


class AudiencePage(BasePage):

    locators = basic_locators.AudiencePageLocators
    segment_name = None

    @allure.step('Clicking on "Create segment"')
    def create_segment(self):
        if self.elements_find(self.locators.CREATE_SEGMENT_BTN_FIRST):
            self.click(self.locators.CREATE_SEGMENT_BTN_FIRST)
        else:
            self.click(self.locators.CREATE_SEGMENT_BTN)

        return CreateSegmentPage(driver=self.driver)

    @allure.step('Discarding a segment')
    def delete_segment(self):
        with allure.step('Composing a cross locator'):
            segment_title_locator = self.format_locator(self.locators.SEGMENT_TITLE_TEMPLATE, self.segment_name)
            row_attribute = self.find(segment_title_locator).get_attribute('data-row-id')
            cross_locator = self.format_locator(self.locators.DELETE_SEGMENT_BTN_TEMPLATE, row_attribute)
        self.click(cross_locator)
        self.click(self.locators.DELETE_BTN)
        wait(method=self.not_on_page, locator=self.locators.DELETE_BTN)
        self.logger.info(f'Segment "{self.segment_name}" is deleted')
