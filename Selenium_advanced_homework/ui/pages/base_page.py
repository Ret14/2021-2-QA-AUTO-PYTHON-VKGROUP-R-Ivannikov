import logging
import string
import random
import time
import allure
from selenium.webdriver import ActionChains
from ui.locators import basic_locators
from utils.decorators import wait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    locators = basic_locators.BasePageLocators

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('test')
        self.logger.info(f'Going on {self.__class__.__name__}')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    @allure.step('Filling up {locator} field')
    def fill_up(self, locator, query):
        self.find(locator).click()
        self.find(locator).clear()
        self.find(locator).send_keys(query)
        self.logger.info(f'Filling up {locator} field')

    @property
    def action_chains(self):
        return ActionChains(self.driver)

    @staticmethod
    def generate_string(length=6):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        random_string = random_string + str(int(time.time()) % 10000)
        return random_string

    def scroll_to(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Clicking on {locator}')
    def click(self, locator, timeout=None):
        self.logger.info(f'Clicking on {locator}')
        for i in range(3):
            try:
                self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                self.scroll_to(elem)
                elem.click()
                return
            except StaleElementReferenceException:
                if i == 2:
                    raise

    def elements_find(self, locator):
        return self.driver.find_elements(locator[0], locator[1])

    def not_on_page(self, locator):
        return not self.elements_find(locator=locator)

    def spinner_wait(self):
        wait(method=self.elements_find, locator=self.locators.SPINNER)
        wait(method=self.not_on_page, locator=self.locators.SPINNER)

    @staticmethod
    def format_locator(locator: tuple, value=None):
        return locator[0], locator[1].format(value)

    def redirect_wait(self, timeout=2, interval=0.5):
        current_url = self.driver.current_url
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.driver.current_url != current_url:
                current_url = self.driver.current_url
                start_time = time.time()
            time.sleep(interval)
        return current_url
