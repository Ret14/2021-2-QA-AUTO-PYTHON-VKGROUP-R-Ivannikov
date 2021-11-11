import logging
import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ui.locators.app_locators import BaseLocators
import allure


class CantSwipeToAnElement(Exception):
    pass


class BasePage(object):

    locators = BaseLocators()
    logger = logging.getLogger('test')

    def __init__(self, driver):
        self.driver = driver
        self.logger.info(f'Going on {self.__class__.__name__}')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Clicking on {locator}')
    def click(self, locator, timeout=None):
        self.logger.info(f'Clicking on {locator}')
        for i in range(3):
            try:
                self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except StaleElementReferenceException:
                if i == 2:
                    raise

    def elements_find(self, locator):
        return self.driver.find_elements(locator[0], locator[1])

    def not_on_page(self, locator):
        return not self.elements_find(locator=locator)

    @staticmethod
    def format_locator(locator: tuple, value=None):
        return locator[0], locator[1].format(value)

    @allure.step('Swiping up')
    def swipe_up(self, duration=400):
        dimension = self.driver.get_window_size()
        x = int(dimension['width'] / 2)
        start_y = int(dimension['height'] * 0.8)
        end_y = int(dimension['height'] * 0.2)
        self.driver.swipe(x, start_y, x, end_y, duration)

    @allure.step('Swiping "{locator}" element left')
    def swipe_element_left(self, locator):
        web_element = self.find(locator)
        left_x = web_element.location['x']
        right_x = left_x + web_element.rect['width']
        upper_y = web_element.location['y']
        lower_y = upper_y + web_element.rect['height']
        middle_y = (upper_y + lower_y) / 2
        self.driver.swipe(right_x, middle_y, left_x, middle_y, 400)

    @allure.step('Swiping up searching for "{locator}"')
    def swipe_up_until_find_elem(self, locator, timeout=5):
        start_time = time.time()
        while time.time() - start_time < timeout:
            self.swipe_up(duration=100)
            if self.elements_find(locator):
                return

        raise CantSwipeToAnElement()

    def text_search(self, query=None):
        return self.elements_find(self.format_locator(self.locators.TEXT_SEARCH, query))
