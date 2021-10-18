from base import BaseCase
from ui.locators import basic_locators
import pytest
from selenium.webdriver.support import expected_conditions as EC


class TestOne(BaseCase):

    @pytest.mark.UI
    def test_login(self, open_and_login):
        assert "Кампании" in self.driver.title

    @pytest.mark.UI
    def test_logout(self, open_and_login):
        self.logout()
        assert 'https://target.my.com/' == self.driver.current_url

    @pytest.mark.UI
    def test_profile_data_changing(self, open_and_login):
        field_value = self.contact_data_save_and_check()
        assert self.find(basic_locators.NAME_FIELD).get_attribute('value') == field_value['name']
        assert self.find(basic_locators.PHONE_FIELD).get_attribute('value') == field_value['phone']

    @pytest.mark.UI
    @pytest.mark.parametrize(
        "locator,title,url",
        [(basic_locators.TOOLS_TAB, 'Список фидов', 'https://target.my.com/tools/feeds'),
        (basic_locators.PRO_TAB, 'myTarget Pro - Блог о таргетированной рекламе', 'https://target.my.com/pro')]
    )
    def test_navigation(self, open_and_login, locator, title, url):
        self.navigate_on(locator)
        self.wait().until(EC.title_is(title))
        assert self.driver.title == title and self.driver.current_url == url
