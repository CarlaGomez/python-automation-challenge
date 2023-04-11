class AuthenticationPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://automationteststore.com/index.php?rt=account/login")

    def fill_personal_details(self, first_name, last_name, email, phone, fax):
        self.page.get_by_role("button", name=" Continue").click()
        self.page.fill("#AccountFrm_firstname", first_name)
        self.page.fill("#AccountFrm_lastname", last_name)
        self.page.fill("#AccountFrm_email", email)
        self.page.fill("#AccountFrm_telephone", phone)
        self.page.fill("#AccountFrm_fax", fax)

    def fill_address(self, company, first_address, second_address, country_id, city, region_id, zip_code):
        self.page.fill("#AccountFrm_company", company)
        self.page.fill("#AccountFrm_address_1", first_address)
        self.page.fill("#AccountFrm_address_2", second_address)
        self.page.locator("#AccountFrm_country_id").select_option(country_id)
        self.page.fill("#AccountFrm_city", city)
        self.page.locator("#AccountFrm_zone_id").select_option(region_id)
        self.page.fill("#AccountFrm_postcode", zip_code)

    def fill_login_details(self, login_name, password):
        self.page.fill("#AccountFrm_loginname", login_name)
        self.page.fill("#AccountFrm_password", password)
        self.page.fill("#AccountFrm_confirm", password)

    def fill_newsletter(self):
        self.page.get_by_label("Yes").check()

    def check_privacy_policy(self):
        self.page.get_by_label("I have read and agree to the Privacy Policy").check()

    def register(self):
        self.page.locator("#AccountFrm div").filter(has_text="Continue").nth(2).click()
        self.page.get_by_role("link", name=" Continue").click()

    def login(self, login_name, password):
        self.page.fill("#loginFrm_loginname", login_name)
        self.page.fill("#loginFrm_password", password)
        self.page.get_by_role("button", name=" Login").click()

    def logout(self):
        self.page.get_by_role("link", name=" Account", exact=True).hover()
        self.page.get_by_role("link", name=" Logout").click()
    