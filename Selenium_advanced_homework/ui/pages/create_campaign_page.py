import logging
import time
import string
import random
import os
import allure
import pytest
from selenium.webdriver import ActionChains
import numpy
from PIL import Image

from ui.locators import basic_locators
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import *
from ui.pages.campaign_page import *


class CreateCampaignPage(BasePage):
    locators = basic_locators.CreateCampaignPageLocators
    title = 'Создать кампанию'
    url = 'https://target.my.com/campaign/new'

    @allure.step('Creating new campaign')
    def create_new_campaign(self, pictures, campaign_page):
        self.click(self.locators.TRAFFIC_BTN)
        content = self.generate_string()
        with allure.step('Filling up link form'):
            self.fill_up(self.locators.LINK_INPUT, content + '.ru')
        self.wait(10).until(EC.visibility_of_element_located(self.locators.CAMPAIGN_NAME_INPUT))
        self.click(self.locators.ROUNDABOUT_TAB)
        self.wait().until(EC.visibility_of_element_located(self.locators.SLIDE_LINK_INPUT))
        self.fill_up(self.locators.AD_TITLE_INPUT, content)
        self.fill_up(self.locators.AD_TEXT_INPUT, content)
        self.fill_up(self.locators.CAMPAIGN_NAME_INPUT, content)
        images = pictures
        with allure.step('Uploading a 256x256 image'):
            self.find(self.locators.IMG_INPUT_256).send_keys(images[256])
        with allure.step('filling up information for each slide'):
            for i in '012':
                slide_number_locator = (self.locators.SLIDE_BTN_TEMPLATE[0],
                                        self.locators.SLIDE_BTN_TEMPLATE[1].format(i)
                                        )
                self.click(slide_number_locator)
                with allure.step('Uploading a 600x600 image'):
                    self.find(self.locators.IMG_INPUT_600).send_keys(images[600])
                with allure.step('Filling up the rest'):
                    self.fill_up(self.locators.SLIDE_LINK_INPUT, content + '.ru')
                    self.fill_up(self.locators.SLIDE_TITLE_INPUT, content)
                with allure.step('Waiting until 600x600 image is uploaded'):
                    wait(method=self.is_on_page, check=True, locator=self.locators.IMG_INPUT_600_BTN_GREEN)

        time.sleep(3)
        self.click(self.locators.SAVE_AD_BTN)
        self.click(self.locators.CREATE_CAMPAIGN_BTN)
        self.logger.info(f'Campaign "{content}" is created')
        with allure.step('Giving the segment name to campaign page'):
            campaign_page.ad_name = content
        return campaign_page
