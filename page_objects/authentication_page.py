# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

from page_objects.commons_page import Base


class AuthenticationPage(Base):
    def navigate(self):
        self.page.goto(f"{self.base_url}/index.php?rt=account/login")

    def is_register_account_option_checked(self, is_checked):
        if is_checked is True:
            assert self.page.locator("#accountFrm_accountregister").is_visible()
        else:
            assert self.page.locator("#accountFrm_accountregister").is_hidden()

    def click_register_button(self):
        return self.page.get_by_role("button", name=" Continue").click()

    def click_continue_button(self):
        return self.page.get_by_role("link", name=" Continue").click()

    def fill_personal_details(self, first_name, last_name, email, phone, fax):
        self.page.fill("#AccountFrm_firstname", first_name)
        self.page.fill("#AccountFrm_lastname", last_name)
        self.page.fill("#AccountFrm_email", email)
        self.page.fill("#AccountFrm_telephone", phone)
        self.page.fill("#AccountFrm_fax", fax)

    def fill_address(
        self,
        company,
        first_address,
        second_address,
        country_id,
        city,
        region_id,
        zip_code,
    ):
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

    def fill_newsletter(self, option):
        return self.page.get_by_label(option).check()

    def check_privacy_policy(self):
        return self.page.get_by_label(
            "I have read and agree to the Privacy Policy"
        ).check()

    def register(self):
        return (
            self.page.locator("#AccountFrm div")
            .filter(has_text="Continue")
            .nth(2)
            .click()
        )

    def is_user_registered_message_displayed(self, is_visible):
        if is_visible is True:
            assert self.page.get_by_text("Your Account Has Been Created!").is_visible()
        else:
            assert self.page.get_by_text("Your Account Has Been Created!").is_hidden()

    def is_user_logged_in(self, is_logged_in):
        if is_logged_in is True:
            assert self.page.get_by_role("link", name="Welcome back John").is_visible()
        else:
            assert self.page.get_by_role("link", name="Welcome back John").is_hidden()

    def login(self, login_name, password):
        self.page.fill("#loginFrm_loginname", login_name)
        self.page.fill("#loginFrm_password", password)
        self.page.get_by_role("button", name=" Login").click()

    def logout(self):
        self.page.get_by_role("link", name=" Account", exact=True).hover()
        self.page.get_by_role("link", name=" Logout").click()

    def is_user_logged_out_message_displayed(self, is_visible):
        if is_visible is True:
            assert self.page.get_by_text("Account Logout", exact=True).is_visible()
        else:
            assert self.page.get_by_text("Account Logout", exact=True).is_hidden()
