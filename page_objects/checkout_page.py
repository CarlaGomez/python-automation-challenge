from playwright.sync_api import expect
from page_objects.commons_page import Base
import time

class CheckoutPage(Base):

    def add_item_to_cart(self, product_quantity):
        self.page.locator("#product_quantity").fill(product_quantity)
        self.page.get_by_role("link", name=" Add to Cart").click()

    async def validate_items_on_shopping_cart(self, page_title, product, quantity):
        time.sleep(3)
        assert self.page.get_by_text(page_title).is_visible()
        assert self.page.get_by_role("cell", name=product).is_visible()
        await expect(self.page.locator("#cart_quantity79")).to_contain_text(quantity)

    def go_to_shopping_cart(self):
        self.page.get_by_role("link", name=" Cart").click()
        time.sleep(3)

    def fill_shipping(self, country_id, state_id, zip_code):
        self.page.locator("#estimate_country").select_option(country_id)
        self.page.locator("#estimate_country_zones").select_option(state_id)
        self.page.locator("#estimate_postcode").fill(zip_code)
        self.page.get_by_role("button", name=" Estimate").click()

    def validate_shipping_info(self):
        time.sleep(3)
        assert self.page.get_by_role("row", name="Sub-Total: $36.00").get_by_role("cell", name="$36.00").nth(4)
        assert self.page.get_by_role("cell", name="$41.06").nth(1)

    def checkout(self):
        self.page.locator("#cart_checkout2").click()

    def validate_checkout_info(self):
        time.sleep(3)
        assert self.page.get_by_role("cell", name="ck One Gift Set", exact=True).is_visible()
        assert self.page.get_by_text("Checkout Confirmation").is_visible()
        assert self.page.get_by_role("cell", name="$41.06").first
        assert self.page.get_by_role("cell", name="$36.00").nth(2)

    def confirm_purchase(self):
        self.page.get_by_role("button", name=" Confirm Order").click()

    def validate_purchase(self):
        time.sleep(3)
        assert self.page.get_by_text("Your Order Has Been Processed!").is_visible()
   