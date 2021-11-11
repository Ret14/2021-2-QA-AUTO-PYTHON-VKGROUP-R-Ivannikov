import allure
from ui.locators.app_locators import MainPageLocators
from ui.pages.base_page import BasePage
from ui.pages.search_page import SearchPage
from ui.pages.settings_page import SettingsPage
from utils.decorators import wait

KEYCODE_VOLUME_DOWN = 25


class MainPage(BasePage):

    locators = MainPageLocators()

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.preparations()

    def preparations(self):
        wait(method=self.elements_find, locator=self.locators.ABILITIES_TAB)
        with allure.step('Muting the volume'):
            for i in range(10):
                self.driver.press_keycode(KEYCODE_VOLUME_DOWN)
        self.click(self.locators.ABILITIES_TAB)
        wait(method=self.elements_find, locator=self.locators.RECORD_BTN)
        self.click(self.locators.RECORD_BTN)

    def go_to_settings_page(self):
        self.click(self.locators.SETTINGS_BTN)
        return SettingsPage(driver=self.driver)

    def go_to_search_page(self):
        self.click(self.locators.KEYBOARD_BTN)
        return SearchPage(driver=self.driver)



