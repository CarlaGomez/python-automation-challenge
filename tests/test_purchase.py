from playwright.sync_api import Page
from page_objects.authentication_page import AuthenticationPage
from page_objects.items_page import ItemsPage
from page_objects.checkout_page import CheckoutPage

def test_search_for_item(page: Page) -> None:
    authentication_page = AuthenticationPage(page)
    items_page = ItemsPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    items_page.search_for_products("Fragrance", "Women")
    items_page.validate_category_name("Fragrance for Women")

def test_sort_by(page: Page) -> None:
    authentication_page = AuthenticationPage(page)
    items_page = ItemsPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    items_page.search_for_products("Fragrance", "Women")
    items_page.validate_category_name("Fragrance for Women")
    items_page.sort_by("p.price-ASC")

def test_view_item_details(page: Page) -> None:
    authentication_page = AuthenticationPage(page)
    items_page = ItemsPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    items_page.search_for_products("Fragrance", "Women")
    items_page.validate_category_name("Fragrance for Women")
    items_page.sort_by("p.price-ASC")
    items_page.go_to_item_details()
    items_page.validate_item_name("ck One Gift Set")
    items_page.validate_item_price("$36.00")

def test_add_item_to_cart(page: Page) -> None:

    authentication_page = AuthenticationPage(page)
    items_page = ItemsPage(page)
    checkout_page = CheckoutPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    items_page.search_for_products("Fragrance", "Women")
    items_page.validate_category_name("Fragrance for Women")
    items_page.sort_by("p.price-ASC")
    items_page.go_to_item_details()
    items_page.validate_item_name("ck One Gift Set")
    items_page.validate_item_price("$36.00")
    checkout_page.add_item_to_cart("1")
    checkout_page.validate_items_on_shopping_cart("Shopping Cart", "ck One Gift Set", "1")

def test_view_shopping_cart(page: Page) -> None:
    authentication_page = AuthenticationPage(page)
    items_page = ItemsPage(page)
    checkout_page = CheckoutPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    items_page.search_for_products("Fragrance", "Women")
    items_page.validate_category_name("Fragrance for Women")
    items_page.sort_by("p.price-ASC")
    items_page.go_to_item_details()
    items_page.validate_item_name("ck One Gift Set")
    items_page.validate_item_price("$36.00")
    checkout_page.add_item_to_cart("1")
    checkout_page.go_to_shopping_cart()
    checkout_page.validate_items_on_shopping_cart("Shopping Cart", "ck One Gift Set", "1")

def test_fill_shipping_information(page: Page) -> None:
    authentication_page = AuthenticationPage(page)
    checkout_page = CheckoutPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    checkout_page.go_to_shopping_cart()
    checkout_page.validate_items_on_shopping_cart("Shopping Cart", "ck One Gift Set", 1)
    checkout_page.fill_shipping("223", "3630", "76876")
    checkout_page.validate_shipping_info("$36.00", "$41.06")

def test_checkout(page: Page) -> None:
    authentication_page = AuthenticationPage(page)
    checkout_page = CheckoutPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    checkout_page.go_to_shopping_cart()
    checkout_page.validate_items_on_shopping_cart("Shopping Cart", "ck One Gift Set", 1)
    checkout_page.fill_shipping("223", "3630", "76876")
    checkout_page.validate_shipping_info("$36.00", "$41.06")
    checkout_page.checkout()
    checkout_page.validate_checkout_info("Checkout Confirmation","ck One Gift Set", "$36.00", "$41.06")

def test_confirm_purchase(page: Page) -> None:
    authentication_page = AuthenticationPage(page)
    checkout_page = CheckoutPage(page)
    
    authentication_page.navigate()
    authentication_page.login("johndoeuser", "johndoepass")
    checkout_page.go_to_shopping_cart()
    checkout_page.validate_items_on_shopping_cart("Shopping Cart", "ck One Gift Set", 1)
    checkout_page.fill_shipping("223", "3631", "76876")
    checkout_page.validate_shipping_info("$36.00", "$41.06")
    checkout_page.checkout()
    checkout_page.validate_checkout_info("Checkout Confirmation","ck One Gift Set", "$36.00", "$41.06")
    checkout_page.confirm_purchase()
    checkout_page.validate_purchase("Your Order Has Been Processed!")
