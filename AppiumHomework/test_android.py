import pytest
from base import BaseCase


@pytest.mark.AndroidUI
class TestSearch(BaseCase):

    def test_search_population(self, search_page):
        search_page.type_text_and_swipe()
        self.make_a_shot('searching_russia_population')
        assert search_page.text_search('146')

    def test_math_equation(self, search_page):
        search_page.do_the_math()
        self.make_a_shot('calculating "2**10"')
        assert search_page.text_search('1024')

    def test_news_fm(self, main_page, news_source_page):
        news_source_page.choose_news_fm()
        self.make_a_shot('news_fm_is_chosen')
        news_source_page.back_to_main_page()
        search_page = main_page.go_to_search_page()
        search_page.type_news()
        self.make_a_shot('launching_news')
        assert search_page.text_search('Вести FM')


@pytest.mark.AndroidUI
class TestAboutApp(BaseCase):

    def test_version_and_trademark(self, about_app_page):
        about_app_page.version_and_trademark_assertions(version=self.app_version)
        self.make_a_shot('about_app_page')
