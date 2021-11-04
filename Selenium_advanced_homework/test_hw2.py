import allure
from base import BaseCase
import pytest


@pytest.mark.UI
class TestLoginNegative(BaseCase):

    @allure.story('Log in negative test')
    def test_false_login(self, credentials):
        url = self.login_page.login(user=self.login_page.generate_string()+'@mail.ru', password=credentials[1])
        self.make_a_shot(name='trying_false_login')
        assert url.startswith('https://target.my.com/dashboard')

    @allure.story('Log in negative test')
    def test_false_password(self, credentials):
        url = self.login_page.login(user=credentials[0], password=self.login_page.generate_string())
        self.make_a_shot(name='trying_false_password')
        assert url.startswith('https://target.my.com/dashboard')


@pytest.mark.UI
class TestAdCreation(BaseCase):

    @allure.story('Campaign creation test')
    def test_campaign_created(self, campaign_page, create_campaign_page, prepare_images):
        campaign_page = create_campaign_page.create_new_campaign(pictures=prepare_images, campaign_page=campaign_page)
        campaign = campaign_page.format_locator(campaign_page.locators.SEARCH_BY_TEXT, campaign_page.ad_name)
        assert campaign_page.elements_find(campaign)
        self.make_a_shot(name=f'campaign_{campaign_page.ad_name}_created')
        campaign_page.delete_campaign()


@pytest.mark.UI
class TestSegment(BaseCase):

    @allure.story('Segment creation test')
    def test_segment_creation(self, audience_page, create_segment_page):
        audience_page = create_segment_page.create_new_segment(audience_page=audience_page)
        segment = audience_page.format_locator(audience_page.locators.SEARCH_BY_TEXT, audience_page.segment_name)
        assert audience_page.elements_find(locator=segment)
        self.make_a_shot(name=f'segment_{audience_page.segment_name}_created')
        audience_page.delete_segment()

    @allure.story('Segment discarding test')
    def test_segment_create_and_discard(self, audience_page, create_segment_page):
        audience_page = create_segment_page.create_new_segment(audience_page=audience_page)
        segment = audience_page.format_locator(audience_page.locators.SEARCH_BY_TEXT, audience_page.segment_name)
        self.make_a_shot(name=f'segment_{audience_page.segment_name}_created')
        audience_page.delete_segment()
        assert audience_page.not_on_page(segment)
        self.make_a_shot(name=f'segment_{audience_page.segment_name}_deleted')
