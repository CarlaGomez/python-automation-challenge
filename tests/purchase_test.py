from playwright.sync_api import Playwright, sync_playwright, expect
from page_objects.authentication_page import AuthenticationPage
from page_objects.items_page import ItemsPage
from page_objects.checkout_page import CheckoutPage

def search_for_item(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    authentication_page = AuthenticationPage(page)
    items_page = ItemsPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    items_page.search_for_fragrances()
    assert page.get_by_text("Fragrance for Women", exact=True).is_visible()

    context.close()
    browser.close()

def sort_by(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    authentication_page = AuthenticationPage(page)
    items_page = ItemsPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    items_page.search_for_fragrances()   
    items_page.sort_by("p.price-ASC")

    context.close()
    browser.close()

def view_item_details(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    authentication_page = AuthenticationPage(page)
    items_page = ItemsPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    items_page.search_for_fragrances()   
    items_page.sort_by("p.price-ASC")
    items_page.view_item_details()

    context.close()
    browser.close()

def add_item_to_cart(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    authentication_page = AuthenticationPage(page)
    items_page = ItemsPage(page)
    checkout_page = CheckoutPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    items_page.search_for_fragrances()
    items_page.sort_by("p.price-ASC")
    items_page.view_item_details()
    checkout_page.add_item_to_cart("1")
    checkout_page.validate_items_on_shopping_cart("Shopping Cart", "ck One Gift Set", "1")
    
    context.close()
    browser.close()

def view_shopping_cart(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    authentication_page = AuthenticationPage(page)
    items_page = ItemsPage(page)
    checkout_page = CheckoutPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    items_page.search_for_fragrances()
    items_page.sort_by("p.price-ASC")
    items_page.view_item_details()
    checkout_page.add_item_to_cart("1")
    checkout_page.go_to_shopping_cart()
    checkout_page.validate_items_on_shopping_cart("Shopping Cart", "ck One Gift Set", "1")
    
    context.close()
    browser.close()

def fill_shipping_information(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    authentication_page = AuthenticationPage(page)
    checkout_page = CheckoutPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    checkout_page.go_to_shopping_cart()
    checkout_page.validate_items_on_shopping_cart("Shopping Cart", "ck One Gift Set", 1)
    checkout_page.fill_shipping("223", "3630", "76876")
    checkout_page.validate_shipping_info()
    
    context.close()
    browser.close()

def checkout(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    authentication_page = AuthenticationPage(page)
    checkout_page = CheckoutPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    checkout_page.go_to_shopping_cart()
    checkout_page.validate_items_on_shopping_cart("Shopping Cart", "ck One Gift Set", 1)
    checkout_page.fill_shipping("223", "3630", "76876")
    checkout_page.validate_shipping_info()
    checkout_page.checkout()
    checkout_page.validate_checkout_info()
    
    context.close()
    browser.close()

def confirm_purchase(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    authentication_page = AuthenticationPage(page)
    checkout_page = CheckoutPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    checkout_page.go_to_shopping_cart()
    checkout_page.validate_items_on_shopping_cart("Shopping Cart", "ck One Gift Set", 1)
    checkout_page.fill_shipping("223", "3631", "76876")
    checkout_page.validate_shipping_info()
    checkout_page.checkout()
    checkout_page.validate_checkout_info()
    checkout_page.confirm_purchase()
    checkout_page.validate_purchase()
    
    context.close()
    browser.close()

with sync_playwright() as playwright:
    search_for_item(playwright)
    sort_by(playwright)
    view_item_details(playwright)
    view_shopping_cart(playwright)
    fill_shipping_information(playwright)
    checkout(playwright)
    confirm_purchase(playwright)
