import time
import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from utils.decorators import wait


class CreateCampaignPage(BasePage):

    locators = basic_locators.CreateCampaignPageLocators

    @allure.step('Creating new campaign')
    def create_new_campaign(self, pictures, campaign_page):
        self.click(self.locators.TRAFFIC_BTN)
        content = self.generate_string() + '.ru'
        with allure.step('Filling up link form'):
            self.fill_up(self.locators.LINK_INPUT, content)
        wait(method=self.elements_find, locator=self.locators.ROUNDABOUT_TAB)
        self.click(self.locators.ROUNDABOUT_TAB)
        wait(method=self.elements_find, locator=self.format_locator(self.locators.SLIDE_LINK_INPUT_TEMPLATE, 1))
        self.fill_up(self.locators.AD_TITLE_INPUT, content)
        self.fill_up(self.locators.AD_TEXT_INPUT, content)
        self.fill_up(self.locators.CAMPAIGN_NAME_INPUT, content)
        images = pictures
        with allure.step('Uploading a 256x256 image'):
            self.find(self.locators.IMG_INPUT_256).send_keys(images[256])
        with allure.step('filling up information for each slide'):
            for i in range(3):
                slide_number_locator = self.format_locator(self.locators.SLIDE_BTN_TEMPLATE, i)
                self.click(slide_number_locator)
                with allure.step('Uploading a 600x600 image'):
                    self.find(self.locators.IMG_INPUT_600).send_keys(images[600])
                slide_link_locator = self.format_locator(self.locators.SLIDE_LINK_INPUT_TEMPLATE, i+1)
                slide_title_locator = self.format_locator(self.locators.SLIDE_TITLE_INPUT_TEMPLATE, i+1)
                with allure.step('Filling up the rest'):
                    self.fill_up(slide_link_locator, content)
                    self.fill_up(slide_title_locator, content)
                with allure.step('Waiting until 600x600 image is uploaded'):
                    wait(method=self.elements_find, locator=self.locators.IMG_INPUT_600_BTN_GREEN)

        time.sleep(1)
        self.click(self.locators.CREATE_CAMPAIGN_BTN)
        self.logger.info(f'Campaign "{content}" is created')
        with allure.step('Giving the campaign name to campaign page'):
            campaign_page.ad_name = content
        return campaign_page
