# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-arguments

import os
from playwright.sync_api import Page
import pytest
from dotenv import load_dotenv
from page_objects.authentication_page import AuthenticationPage
from page_objects.items_page import ItemsPage
from page_objects.checkout_page import CheckoutPage

load_dotenv()

login_name = os.getenv("LOGIN_NAME")
login_password = os.getenv("LOGIN_PASSWORD")

test_search_for_item_data = [
    ("Fragrance", "Women", "Fragrance for Women"),
]

test_sort_by_data = [
    ("p.price-ASC"),
]

item_name_data = [
    ("ck One Gift Set"),
]

item_price_data = [
    ("$36.00"),
]

product_data = [
    ("ck One Gift Set", "$36.00", "$41.06"),
]

shipping_data = [
    ("223", "3630", "76876"),
]


@pytest.mark.parametrize("product, gender, product_category", test_search_for_item_data)
def test_search_for_item(page: Page, product, gender, product_category) -> None:
    print(os.getenv("USER"))

    authentication_page = AuthenticationPage(page)
    items_page = ItemsPage(page)
    authentication_page.navigate()
    authentication_page.login(login_name, login_password)
    items_page.search_for_products(product, gender)
    items_page.validate_category_name(product_category)


@pytest.mark.parametrize("product, gender, product_category", test_search_for_item_data)
@pytest.mark.parametrize("sort_criteria", test_sort_by_data)
def test_sort_by(page: Page, product, gender, product_category, sort_criteria) -> None:
    authentication_page = AuthenticationPage(page)
    items_page = ItemsPage(page)
    authentication_page.navigate()
    authentication_page.login(login_name, login_password)
    items_page.search_for_products(product, gender)
    items_page.validate_category_name(product_category)
    items_page.sort_by(sort_criteria)


@pytest.mark.parametrize("product, gender, product_category", test_search_for_item_data)
@pytest.mark.parametrize("sort_criteria", test_sort_by_data)
@pytest.mark.parametrize("item_name", item_name_data)
@pytest.mark.parametrize("item_price", item_price_data)
def test_view_item_details(
    page: Page, product, gender, product_category, sort_criteria, item_name, item_price
) -> None:
    authentication_page = AuthenticationPage(page)
    items_page = ItemsPage(page)
    authentication_page.navigate()
    authentication_page.login(login_name, login_password)
    items_page.search_for_products(product, gender)
    items_page.validate_category_name(product_category)
    items_page.sort_by(sort_criteria)
    items_page.go_to_item_details()
    items_page.validate_item_name(item_name)
    items_page.validate_item_price(item_price)


@pytest.mark.parametrize("product, gender, product_category", test_search_for_item_data)
@pytest.mark.parametrize("sort_criteria", test_sort_by_data)
@pytest.mark.parametrize("item_name", item_name_data)
@pytest.mark.parametrize("item_price", item_price_data)
def test_add_item_to_cart(
    page: Page, product, gender, product_category, sort_criteria, item_name, item_price
) -> None:
    authentication_page = AuthenticationPage(page)
    items_page = ItemsPage(page)
    checkout_page = CheckoutPage(page)
    authentication_page.navigate()
    authentication_page.login(login_name, login_password)
    items_page.search_for_products(product, gender)
    items_page.validate_category_name(product_category)
    items_page.sort_by(sort_criteria)
    items_page.go_to_item_details()
    items_page.validate_item_name(item_name)
    items_page.validate_item_price(item_price)
    checkout_page.add_item_to_cart("1")
    checkout_page.validate_items_on_shopping_cart("Shopping Cart", item_name, "1")


@pytest.mark.parametrize("item_name", item_name_data)
def test_view_shopping_cart(page: Page, item_name) -> None:
    authentication_page = AuthenticationPage(page)
    checkout_page = CheckoutPage(page)

    authentication_page.navigate()
    authentication_page.login(login_name, login_password)
    checkout_page.go_to_shopping_cart()
    checkout_page.validate_items_on_shopping_cart("Shopping Cart", item_name, "1")


@pytest.mark.parametrize("item_name, item_price, total_price", product_data)
@pytest.mark.parametrize("country_id, region_id, zipcode", shipping_data)
def test_fill_shipping_information(
    page: Page, item_name, item_price, total_price, country_id, region_id, zipcode
) -> None:
    authentication_page = AuthenticationPage(page)
    checkout_page = CheckoutPage(page)

    authentication_page.navigate()
    authentication_page.login(login_name, login_password)
    checkout_page.go_to_shopping_cart()
    checkout_page.validate_items_on_shopping_cart("Shopping Cart", item_name, 1)
    checkout_page.fill_shipping(country_id, region_id, zipcode)
    checkout_page.validate_shipping_info(item_price, total_price)


@pytest.mark.parametrize("item_name, item_price, total_price", product_data)
@pytest.mark.parametrize("country_id, region_id, zipcode", shipping_data)
def test_checkout(
    page: Page, item_name, item_price, total_price, country_id, region_id, zipcode
) -> None:
    authentication_page = AuthenticationPage(page)
    checkout_page = CheckoutPage(page)

    authentication_page.navigate()
    authentication_page.login(login_name, login_password)
    checkout_page.go_to_shopping_cart()
    checkout_page.validate_items_on_shopping_cart("Shopping Cart", item_name, 1)
    checkout_page.fill_shipping(country_id, region_id, zipcode)
    checkout_page.validate_shipping_info(item_price, total_price)
    checkout_page.checkout()
    checkout_page.validate_checkout_info(
        "Checkout Confirmation", item_name, item_price, total_price
    )


@pytest.mark.parametrize("item_name, item_price, total_price", product_data)
@pytest.mark.parametrize("country_id, region_id, zipcode", shipping_data)
def test_confirm_purchase(
    page: Page, item_name, item_price, total_price, country_id, region_id, zipcode
) -> None:
    authentication_page = AuthenticationPage(page)
    checkout_page = CheckoutPage(page)

    authentication_page.navigate()
    authentication_page.login(login_name, login_password)
    checkout_page.go_to_shopping_cart()
    checkout_page.validate_items_on_shopping_cart("Shopping Cart", item_name, 1)
    checkout_page.fill_shipping(country_id, region_id, zipcode)
    checkout_page.validate_shipping_info(item_price, total_price)
    checkout_page.checkout()
    checkout_page.validate_checkout_info(
        "Checkout Confirmation", item_name, item_price, total_price
    )
    checkout_page.confirm_purchase()
    checkout_page.validate_purchase("Your Order Has Been Processed!")
