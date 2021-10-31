import logging
import time
import string
import random

import allure
from selenium.webdriver import ActionChains

from ui.locators import basic_locators
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import *


class CreateSegmentPage(BasePage):

    locators = basic_locators.CreateSegmentPageLocators
    title = 'Новый сегмент'
    url = 'https://target.my.com/segments/segments_list/new/'

    @allure.step('Creating a segment')
    def create_new_segment(self, audience_page):
        self.click(self.locators.SEGMENT_TYPE_TAB)
        self.click(self.locators.SEGMENT_TYPE_CHECKBOX)
        self.click(self.locators.ADD_SEGMENT_BTN)
        content = self.generate_string()
        self.fill_up(self.locators.SEGMENT_NAME_INPUT, content)
        self.click(self.locators.CREATE_SEGMENT_BTN)
        self.logger.info(f'Segment "{content}" is created')
        time.sleep(1)
        with allure.step('Giving the segment name to audience_page'):
            audience_page.segment_name = content
        return audience_page
