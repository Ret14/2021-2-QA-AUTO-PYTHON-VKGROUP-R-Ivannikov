import os
import time
from contextlib import contextmanager

import allure
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from _pytest.fixtures import FixtureRequest

from base import BaseCase
from ui.locators import basic_locators
import pytest


@pytest.mark.UI
class TestLoginNegative(BaseCase):
    authorize_fail = True

    @allure.story('Log in negative test')
    def test_false_login(self, credentials):
        self.login_page.false_login(*credentials, false_login=True)
        self.login_page.make_a_shot(name='trying_false_login', path=self.path)
        assert 'https://account.my.com/login/?error_code=1' in self.login_page.driver.current_url

    @allure.story('Log in negative test')
    def test_false_password(self, credentials):
        self.login_page.false_login(*credentials, false_password=True)
        self.login_page.make_a_shot(name='trying_false_password', path=self.path)
        assert 'https://account.my.com/login/?error_code=1' in self.login_page.driver.current_url


@pytest.mark.UI
class TestAdCreation(BaseCase):
    authorize = False

    @allure.story('Campaign creation test')
    def test_campaign_created(self, prepare_images):
        campaign_page = self.campaign_page
        create_campaign_page = campaign_page.create_campaign()
        campaign_page = create_campaign_page.create_new_campaign(pictures=prepare_images, campaign_page=campaign_page)
        assert campaign_page.ad_name in campaign_page.driver.page_source
        campaign_page.make_a_shot(name=f'new_campaign_was_created', path=self.path)
        campaign_page.delete_campaign()


@pytest.mark.UI
class TestSegment(BaseCase):
    authorize = False

    @allure.story('Segment creation test')
    def test_segment_creation(self):
        campaign_page = self.campaign_page
        audience_page = campaign_page.go_to_audience_page()
        create_segment_page = audience_page.create_segment()
        audience_page = create_segment_page.create_new_segment(audience_page=audience_page)
        segment = (audience_page.locators.SEGMENT_NAME_TEMPLATE[0],
                   audience_page.locators.SEGMENT_NAME_TEMPLATE[1].format(audience_page.segment_name)
                   )
        assert audience_page.is_on_page(segment)
        audience_page.make_a_shot(name=f'new_segment_was_created', path=self.path)
        audience_page.delete_segment()

    @allure.story('Segment discarding test')
    def test_segment_create_and_discard(self):
        campaign_page = self.campaign_page
        audience_page = campaign_page.go_to_audience_page()
        create_segment_page = audience_page.create_segment()
        audience_page = create_segment_page.create_new_segment(audience_page=audience_page)
        segment = (audience_page.locators.SEGMENT_NAME_TEMPLATE[0],
                   audience_page.locators.SEGMENT_NAME_TEMPLATE[1].format(audience_page.segment_name)
                   )
        audience_page.make_a_shot(name=f'new_segment_was_created', path=self.path)
        audience_page.delete_segment()
        assert audience_page.is_not_on_page(segment)
        audience_page.make_a_shot(name=f'segment_was_deleted', path=self.path)



