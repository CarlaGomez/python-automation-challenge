from page_objects.commons_page import Base
import time

class ItemsPage(Base):

    def search_for_products(self, product, gender):
        self.page.get_by_role("link", name=product).hover()
        self.page.get_by_role("link", name=gender).click()

    def sort_by(self, sort_criteria):
        return self.page.locator("#sort").select_option(sort_criteria)

    def go_to_item_details(self):
        time.sleep(2)
        return self.page.locator("div:nth-child(3) > .thumbnail > a").click()

    def validate_item_name(self, item):
        item_name = self.page.get_by_role("heading", name="ck One Gift Set").get_by_text(item)
        assert item_name

    def validate_item_price(self, price):
        item_price = self.page.get_by_text(price).first
        assert item_price


    def validate_category_name(self, category_name):
        time.sleep(2)
        assert self.page.get_by_text(category_name, exact=True).is_visible()
