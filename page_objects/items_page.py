from page_objects.commons_page import Base

class ItemsPage(Base):


    def search_for_fragances(self):
        self.page.get_by_role("link", name="FRAGANCE").hover()
        self.page.get_by_role("link", name="Women").click()

    def fragances_for_women_heading(self):
        assert self.page.get_by_text("Fragrance for Women").is_visible()     

    def sort_by(self, sort_criteria):
        self.page.locator("#sort").select_option(sort_criteria)

    def view_item_details(self):
        self.page.get_by_role("link", name="View", exact=True).click()
