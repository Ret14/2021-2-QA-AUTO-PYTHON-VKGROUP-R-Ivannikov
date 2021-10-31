import logging
import os
import time
import string
import random

import allure
import pytest
from selenium.webdriver import ActionChains

from ui.locators import basic_locators
from utils.decorators import wait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from ui.pages.campaign_page import *

CLICK_RETRY = 3
BASE_TIMEOUT = 10


class BasePage(object):

    url = 'https://target.my.com/'
    title = 'Рекламная платформа myTarget — Сервис таргетированной рекламы'
    locators = basic_locators.BasePageLocators

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('test')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def fill_up(self, locator, query):
        self.find(locator).click()
        self.find(locator).clear()
        self.find(locator).send_keys(query)

    def elements_find(self, locator):
        return self.driver.find_elements(locator[0], locator[1])

    def login(self, user, password):
        self.find(self.locators.LOGIN_BTN).click()
        self.fill_up(self.locators.EMAIL_FIELD, user)
        self.fill_up(self.locators.PASSWORD_FIELD, password + Keys.RETURN)
        self.logger.info('Logging in')

    def false_login(self, login, password, false_login=False, false_password=False):
        self.wait(10).until(EC.visibility_of_element_located(self.locators.LOGIN_BTN))
        self.wait().until(EC.element_to_be_clickable(self.locators.LOGIN_BTN))
        self.find(self.locators.LOGIN_BTN).click()
        if false_login:
            login = self.generate_string()
            login = login + '@mail.ru'
            self.logger.info('Trying to login with false login ({login})')
        if false_password:
            password = self.generate_string()
            self.logger.info('Trying to login with false password ({password})')
        self.fill_up(self.locators.EMAIL_FIELD, login)
        self.fill_up(self.locators.PASSWORD_FIELD, password + Keys.RETURN)

    @property
    def action_chains(self):
        return ActionChains(self.driver)

    @staticmethod
    def generate_string(length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def scroll_to(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Clicking on {locator}')
    def click(self, locator, timeout=None):
        self.logger.info(f'Clicking on {locator}')
        for i in range(CLICK_RETRY):
            try:
                self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                self.scroll_to(elem)
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY-1:
                    raise

    def is_on_page(self, locator):
        if self.elements_find(locator=locator):
            return True
        return False

    def is_not_on_page(self, locator):
        if not self.elements_find(locator=locator):
            return True
        return False

    def spinner_wait(self):
        wait(method=self.is_on_page, check=True, locator=self.locators.SPINNER)
        wait(method=self.is_not_on_page, check=True, locator=self.locators.SPINNER)

    def make_a_shot(self, name='', path=None):
        name = name + '.png'
        screenshot = os.path.join(path, name)
        self.driver.get_screenshot_as_file(screenshot)
        allure.attach.file(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
