# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

import time
from page_objects.commons_page import Base


class CheckoutPage(Base):
    def add_item_to_cart(self, product_quantity):
        self.page.locator("#product_quantity").fill(product_quantity)
        self.page.get_by_role("link", name=" Add to Cart").click()

    def validate_items_on_shopping_cart(self, page_title, product, quantity):
        time.sleep(2)
        assert self.page.get_by_text(page_title).is_visible()
        assert self.page.get_by_role("cell", name=product).is_visible()
        assert self.page.locator("#cart_quantity79").get_by_text(quantity)

    def go_to_shopping_cart(self):
        self.page.get_by_role("link", name=" Cart").click()

    def fill_shipping(self, country_id, region_id, zip_code):
        self.page.locator("#estimate_country").select_option(country_id)
        self.page.locator("#estimate_country_zones").select_option(region_id)
        self.page.locator("#estimate_postcode").fill(zip_code)
        self.page.get_by_role("button", name=" Estimate").click()

    def validate_shipping_info(self, subtotal, total):
        assert (
            self.page.get_by_role("row", name="Sub-Total: $36.00")
            .get_by_role("cell", name=subtotal)
            .nth(4)
        )
        assert self.page.get_by_role("cell", name=total).nth(1)

    def checkout(self):
        self.page.locator("#cart_checkout2").click()

    def validate_checkout_info(self, page_name, item_name, subtotal, total):
        assert self.page.get_by_text(page_name).is_visible()
        assert self.page.get_by_role("cell", name=item_name, exact=True).is_visible()
        assert self.page.get_by_role("cell", name=subtotal).nth(2)
        assert self.page.get_by_role("cell", name=total).first

    def confirm_purchase(self):
        self.page.get_by_role("button", name=" Confirm Order").click()

    def validate_purchase(self, order_confirmation_message):
        time.sleep(3)
        assert self.page.get_by_text(order_confirmation_message).is_visible()
