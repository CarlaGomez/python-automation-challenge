from playwright.sync_api import Playwright, sync_playwright, expect

from page_objects.authentication_page import AuthenticationPage

def register_user(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    authentication_page = AuthenticationPage(page)
    
    authentication_page.navigate()
    authentication_page.fill_personal_details("John", "Doe", "johndoetest1@gmail.com", "18009098990", "18009098991")
    authentication_page.fill_address("Vandelay Industries", "Doral Florida", "FL", "223", "Florida", "3630", "2312")
    authentication_page.fill_login_details("johndoeuser1", "johndoepass")
    authentication_page.fill_newsletter()
    authentication_page.check_privacy_policy()
    authentication_page.register()

    context.close()
    browser.close()

def login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    authentication_page = AuthenticationPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")

    context.close()
    browser.close()

def logout(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    authentication_page = AuthenticationPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    authentication_page.logout()

    context.close()
    browser.close()

with sync_playwright() as playwright:
    register_user(playwright)
    login(playwright)
    logout(playwright)
