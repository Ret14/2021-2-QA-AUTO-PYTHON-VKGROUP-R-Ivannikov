import logging
import time
import string
import random

import allure
from selenium.webdriver import ActionChains
from utils.decorators import wait
from ui.locators import basic_locators
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import *
from ui.pages.create_campaign_page import *
from ui.pages.audience_page import *


class CampaignPage(BasePage):

    locators = basic_locators.CampaignPageLocators
    title = 'Кампании'
    ad_name = None
    url = 'https://target.my.com/dashboard'

    @allure.step('Clicking on "Create campaign" button')
    def create_campaign(self):
        time.sleep(5)
        if self.driver.find_elements(self.locators.FIRST_CREATE_BTN[0], self.locators.FIRST_CREATE_BTN[1]):
            self.click(self.locators.FIRST_CREATE_BTN)
        else:
            self.click(self.locators.CREATE_BTN)
        time.sleep(3)
        self.logger.info(f'Going on {CreateCampaignPage.__name__}')
        return CreateCampaignPage(driver=self.driver)

    @allure.step('Discarding a campaign')
    def delete_campaign(self):
        with allure.step('Composing a settings locator'):
            ad_title_locator = (self.locators.CAMPAIGN_TITLE_PATTERN[0],
                                self.locators.CAMPAIGN_TITLE_PATTERN[1].format(self.ad_name)
                                )
            row_attribute = self.find(ad_title_locator).get_attribute('data-row-id')
            settings_locator = (self.locators.CAMPAIGN_SETTINGS_PATTERN[0],
                                self.locators.CAMPAIGN_SETTINGS_PATTERN[1].format(row_attribute)
                                )
        self.click(settings_locator)
        self.click(self.locators.DELETE_AD_BTN)
        self.logger.info(f'Campaign "{self.ad_name}" is deleted')
        self.driver.refresh()

    @allure.step('Going to "audience page"')
    def go_to_audience_page(self):
        self.click(self.locators.AUDIENCE_BTN)
        self.spinner_wait()
        self.logger.info(f'Going on {AudiencePage.__name__}')
        return AudiencePage(driver=self.driver)

