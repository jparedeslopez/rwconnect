from test_auto.tests.base import BaseTest
from test_auto.pages.home import HomePage
from test_auto.pages.contact_edit import ContactEditPage
from test_auto.pages.contact import ContactPage
from test_auto.pages.contacts_list import ContactsListPage


class TestScenario01(
    BaseTest,
    HomePage,
    ContactEditPage,
    ContactPage,
    ContactsListPage
):

    def test_01_01_PhoneNumberAddition(self):
        '''
        I. Locates the entry for “Mic Pringle”
        II. Taps the information icon for this entry
        III. Verifies that the “Phone Number” text field is empty
        IV. Enters a phone number in the “Phone Number” text field
        V. Taps the “Save” button
        VI. Confirms the successful save operation
        VII. Verifies that the “Phone Number” text field contains the phone number
        '''

        HomePage.open_info_button(self)
        phone_number = ContactEditPage.get_phone_number(self)
        self.assertEqual(phone_number, "Phone Number")
        ContactEditPage.enter_phone_number(self)
        ContactEditPage.back_to_home(self)
        HomePage.open_contact(self)
        self.assertEqual(ContactPage.find_phone_number(self), int(ContactEditPage.PHONE_NUMBER))


        '''TODO:
        - Invalid input data for the phone number.
        - Verfication should not only be done when coming from contacts edition screen, but also when coming directly
        from the home screen. This is actually a bug in current app.
        '''

    def test_01_02_ContactAddition(self):
        '''
        I. Verifies there is no entry for the contact “Kate Bell”
        II. Taps the “+” icon in the top right - hand corner
        III. Selects the "Kate Bell" entry
        IV. Taps the “Done” button in the top right - hand corner
        V. Verifies that there is an entry for the contact “Kate Bell”
        '''

        self.assertIsNone(HomePage.look_for_friend(self))
        HomePage.add_new_contact(self)
        ContactsListPage.add_contact(self)
        self.assertIsNotNone(HomePage.look_for_friend(self))

        '''TODO:
        - Verfication should not only be done when coming from contacts screen, but also when starting the app.
        This is actually a bug in current app.
                '''