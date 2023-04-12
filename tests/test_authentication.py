from playwright.sync_api import Page
from page_objects.authentication_page import AuthenticationPage
from faker import Faker

def test_register_user(page: Page) -> None:
    authentication_page = AuthenticationPage(page)
    fake = Faker()
        
    authentication_page.navigate()
    authentication_page.is_register_account_option_checked(True)
    authentication_page.click_register_button()
    authentication_page.fill_personal_details(fake.first_name(), fake.last_name(), fake.email(), fake.phone_number(), fake.phone_number())
    authentication_page.fill_address(fake.company(), fake.street_address(), fake.address(), "223", fake.city(), "3630", "2312")
    authentication_page.fill_login_details(fake.user_name(), "fakeuserpass")
    authentication_page.fill_newsletter("Yes")
    authentication_page.check_privacy_policy()
    authentication_page.register()
    authentication_page.is_user_registered_message_displayed(True)
    authentication_page.click_continue_button()

def test_login(page: Page) -> None:
    authentication_page = AuthenticationPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    authentication_page.is_user_logged_in(True)

def test_logout(page: Page) -> None:
    authentication_page = AuthenticationPage(page)
    
    authentication_page.navigate()
    authentication_page.is_user_logged_in(False)
    authentication_page.login("johndoeuser", "johndoepass")
    authentication_page.is_user_logged_in(True)
    authentication_page.logout()
    authentication_page.is_user_logged_in(False)
    authentication_page.is_user_logged_out_message_displayed(True)
