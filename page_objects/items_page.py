from page_objects.commons_page import Base
import time

class ItemsPage(Base):

    def search_for_fragrances(self):
        self.page.get_by_role("link", name="Fragrance").hover()
        self.page.get_by_role("link", name="Women").click()
        time.sleep(3)

    def sort_by(self, sort_criteria):
        self.page.locator("#sort").select_option(sort_criteria)

    def view_item_details(self):
        time.sleep(3)
        self.page.locator("div:nth-child(3) > .thumbnail > a").click()

    def product_name(self):
        return self.page.locator(".prdocutname:nth-child(0)")

