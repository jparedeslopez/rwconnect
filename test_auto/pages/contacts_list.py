from .base import BasePage
from appium.webdriver.common.mobileby import MobileBy


class ContactsListPage(BasePage):

    # ===================
    # Inherited Constants
    # ===================
    driver = None
    logger = None

    # =========
    # Test Data
    # =========



    # ========
    # Locators
    # ========

    DONE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Done')
    KATE_CONTACT = (MobileBy.XPATH, '//XCUIElementTypeCell[@name="Kate Bell"]')

    # ============
    # Page Methods
    # ============

    def add_contact(self):
        self.get_element(self.KATE_CONTACT).click()
        self.get_element(self.DONE_BUTTON).click()
