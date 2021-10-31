import logging
import time
import string
import random

import allure
from selenium.webdriver import ActionChains
from ui.pages.base_page import *
from ui.pages.create_segment_page import *


class AudiencePage(BasePage):
    locators = basic_locators.AudiencePageLocators
    title = 'Список сегментов'
    segment_name = None
    url = 'https://target.my.com/segments/segments_list'

    @allure.step('Clicking on "Create segment"')
    def create_segment(self):
        if self.elements_find(self.locators.CREATE_SEGMENT_BTN_FIRST):
            self.click(self.locators.CREATE_SEGMENT_BTN_FIRST)
        else:
            self.click(self.locators.CREATE_SEGMENT_BTN)

        self.logger.info(f'Going on {CreateSegmentPage.__name__}')
        return CreateSegmentPage(driver=self.driver)

    @allure.step('Discarding a segment')
    def delete_segment(self):
        with allure.step('Composing a cross locator'):
            segment_title_locator = (self.locators.SEGMENT_TITLE_TEMPLATE[0],
                                     self.locators.SEGMENT_TITLE_TEMPLATE[1].format(self.segment_name)
                                     )
            row_attribute = self.find(segment_title_locator).get_attribute('data-row-id')
            cross_locator = (self.locators.DELETE_SEGMENT_BTN_TEMPLATE[0],
                             self.locators.DELETE_SEGMENT_BTN_TEMPLATE[1].format(row_attribute)
                             )
        self.click(cross_locator)
        self.click(self.locators.DELETE_BTN)
        self.logger.info(f'Segment "{self.segment_name}" is deleted')
        self.driver.refresh()
