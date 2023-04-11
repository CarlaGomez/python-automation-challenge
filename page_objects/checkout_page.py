from page_objects.commons_page import Base

class CheckoutPage(Base):

    def add_item_to_cart(self, product_quantity):
        self.locator("#product_quantity").fill(product_quantity)
        self.page.get_by_role("link", name=" Add to Cart").click()

    def validate_items_on_shopping_cart(self):
        self.page.get_by_text("Shopping Cart").click()

    def fill_shipping_information(self, country_id, zip_code, subtotal, total):
        self.page.locator("#estimate_country_zones").select_option(country_id)
        self.page.locator("#estimate_postcode").fill(zip_code)
        self.page.get_by_role("button", name=" Estimate").click()
        self.page.get_by_role("row", name="Sub-Total: $72.00").get_by_text(subtotal).click()
        self.page.get_by_text(total).click()
        self.page.locator("#cart_checkout2").click()

    def checkout(self):
        self.page.get_by_label("Yes").check()

    def confirm_purchase(self):
       return self.page.page.get_by_role("heading", name="Checkout Confirmation")

    def confirm_purchase(self):
       return self.page.page.get_by_role("heading", name="Checkout Confirmation")