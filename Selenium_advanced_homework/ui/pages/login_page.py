from selenium.webdriver.common.keys import Keys
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from utils.decorators import wait


class LoginPage(BasePage):

    locators = basic_locators.LoginPageLocators

    def login(self, user, password):
        wait(method=self.elements_find, locator=self.locators.LOGIN_BTN)
        self.click(self.locators.LOGIN_BTN)
        self.fill_up(self.locators.EMAIL_FIELD, user)
        self.fill_up(self.locators.PASSWORD_FIELD, password + Keys.RETURN)
        current_url = self.redirect_wait(timeout=2)
        return current_url
        # if current_url.startswith('https://target.my.com/dashboard'):
        #     return CampaignPage(driver=self.driver)
        # else:
        #     return current_url
