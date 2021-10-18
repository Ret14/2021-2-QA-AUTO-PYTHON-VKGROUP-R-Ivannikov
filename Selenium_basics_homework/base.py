import pytest
import time
import random
from ui.locators import basic_locators
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


CLICK_RETRY = 3

class BaseCase:

    driver = None

    @pytest.fixture(scope='function')
    def open_and_login(self, page_open):
        self.driver = page_open
        self.wait(15).until_not(EC.presence_of_element_located(basic_locators.SPINNER))
        self.wait(15).until(EC.presence_of_element_located(basic_locators.LOGIN_BTN))
        self.wait().until(EC.visibility_of_element_located(basic_locators.LOGIN_BTN))
        self.find(basic_locators.LOGIN_BTN).click()
        self.find(basic_locators.EMAIL_FIELD).send_keys('gengor.gennady@yandex.ru')
        self.find(basic_locators.PASSWORD_FIELD).send_keys('retro66DF@')
        self.find(basic_locators.PASSWORD_FIELD).send_keys(Keys.RETURN)
        self.wait().until(EC.title_is('Кампании'))

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator, timeout)
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY-1:
                    raise
            except NoSuchElementException:
                if i == CLICK_RETRY-1:
                    raise
            except ElementClickInterceptedException:
                if i == CLICK_RETRY-1:
                    raise

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout)

    def login(self):
        self.wait(15).until_not(EC.presence_of_element_located(basic_locators.SPINNER))
        self.wait(15).until(EC.presence_of_element_located(basic_locators.LOGIN_BTN))
        self.wait().until(EC.visibility_of_element_located(basic_locators.LOGIN_BTN))
        self.find(basic_locators.LOGIN_BTN).click()
        self.find(basic_locators.EMAIL_FIELD).send_keys('gengor.gennady@yandex.ru')
        self.find(basic_locators.PASSWORD_FIELD).send_keys('retro66DF@')
        self.find(basic_locators.PASSWORD_FIELD).send_keys(Keys.RETURN)
        self.wait().until(EC.title_is('Кампании'))

    def logout(self):
        self.find(basic_locators.ACCOUNT_TAB).click()
        self.wait().until(EC.visibility_of_element_located(basic_locators.LOGOUT_TAB))
        time.sleep(2)
        self.find(basic_locators.LOGOUT_TAB).click()
        self.wait().until(EC.visibility_of_element_located(basic_locators.LOGIN_BTN))

    def contact_data_save_and_check(self):
        self.find(basic_locators.PROFILE_BTN).click()
        self.wait().until(EC.element_to_be_clickable(basic_locators.SAVE_BTN))
        name_insides = str(random.randint(10, 100))
        self.find(basic_locators.NAME_FIELD).click()
        self.find(basic_locators.NAME_FIELD).clear()
        self.find(basic_locators.NAME_FIELD).send_keys(name_insides)
        phone_insides = str(random.randint(10, 100))
        self.find(basic_locators.PHONE_FIELD).click()
        self.find(basic_locators.PHONE_FIELD).clear()
        self.find(basic_locators.PHONE_FIELD).send_keys(phone_insides)
        self.find(basic_locators.SAVE_BTN).click()
        self.wait().until(EC.element_to_be_clickable(basic_locators.SAVE_BTN))
        self.driver.refresh()
        self.wait(10).until_not(EC.visibility_of_element_located(basic_locators.PHONE_FIELD))
        return {'name': name_insides, 'phone': phone_insides}

    def navigate_on(self, locator):
        prev_title = self.driver.title
        self.find(locator).click()
        self.wait(10).until_not(EC.title_is(prev_title))




