from .base import BasePage
from appium.webdriver.common.mobileby import MobileBy


class HomePage(BasePage):

    # ===================
    # Inherited Constants
    # ===================
    driver = None
    logger = None

    # =========
    # Test Data
    # =========

    MIC_TEXT = "Mic Pringle"
    KATE_TEXT = "Kate Bell"

    # ========
    # Locators
    # ========

    FRIENDS = (MobileBy.ACCESSIBILITY_ID, "friends")
    INFO_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton')
    MIC = (MobileBy.ACCESSIBILITY_ID, MIC_TEXT)
    KATE = (MobileBy.ACCESSIBILITY_ID, KATE_TEXT)
    PLUS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeNavigationBar[@name="RWConnect"]/XCUIElementTypeButton')

    # ============
    # Page Methods
    # ============

    def open_info_button(self):
        friends_list = self.get_elements(self.FRIENDS)
        mic_element = None
        for friend in friends_list:
            if self.get_elements(locator=self.MIC, base_elem=friend):
                mic_element = friend
                break
        self.get_element(base_elem=mic_element, locator=self.INFO_BUTTON).click()

    def open_contact(self):
        friends_list = self.get_elements(self.FRIENDS)
        mic_element = None
        for friend in friends_list:
            if self.get_elements(locator=self.MIC, base_elem=friend):
                mic_element = friend
                break
        self.get_element(base_elem=mic_element, locator=self.MIC).click()

    def look_for_friend(self):
        friends_list = self.get_elements(self.FRIENDS)
        for friend in friends_list:
            if self.get_elements(locator=self.KATE, base_elem=friend):
                return friend

    def add_new_contact(self):
        self.get_element(HomePage.PLUS_BUTTON).click()

        '''
        TO DO:
        - Names are hardcoded here. In the test page, I should give the test data I want instead.
        - open_info_button and open_contact are basically the same. I should write a common function that can be used by
        both of them.
        '''

