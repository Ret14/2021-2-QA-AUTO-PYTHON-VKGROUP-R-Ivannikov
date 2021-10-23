from base import BaseCase
from ui.locators import basic_locators
from funcs import extract_from_file
import pytest
from selenium.webdriver.support import expected_conditions as EC


class TestOne(BaseCase):

    @pytest.mark.UI
    @pytest.mark.usefixtures('open_and_login')
    def test_login(self):
        assert 'Кампании' in self.driver.title

    @pytest.mark.UI
    @pytest.mark.usefixtures('open_and_login')
    def test_logout(self):
        self.logout()
        assert extract_from_file(str_number=3) == self.driver.current_url

    @pytest.mark.UI
    @pytest.mark.usefixtures('open_and_login')
    def test_profile_data_changing(self):
        field_value = self.contact_data_update()
        assert self.find(basic_locators.NAME_FIELD).get_attribute('value') == field_value['name']
        assert self.find(basic_locators.PHONE_FIELD).get_attribute('value') == field_value['phone']

    @pytest.mark.UI
    @pytest.mark.usefixtures('open_and_login')
    @pytest.mark.parametrize(
        "locator,title,url",
        [(basic_locators.TOOLS_BTN, 'Список фидов', extract_from_file(str_number=4)),
         (basic_locators.PRO_BTN, 'myTarget Pro - Блог о таргетированной рекламе', extract_from_file(str_number=5))]
    )
    def test_navigation(self, locator, title, url):
        self.navigate_on(locator)
        self.wait().until(EC.title_is(title))
        assert self.driver.title == title and self.driver.current_url == url
