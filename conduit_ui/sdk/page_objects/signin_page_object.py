from page_objects import PageObject, PageElement

from conduit_ui.sdk.page_objects.navigate_page_object import PageElementNotFound


class SignInPageObject(PageObject):
    email = PageElement(xpath='//input[@placeholder="Email"]')
    password = PageElement(xpath='//input[@placeholder="Password"]')
    sign_in = PageElement(xpath='//button[text()="Sign in"]')
    no_sign_in_disabled_element = PageElementNotFound(xpath='//button[text()="Sign in" and @disabled]', timeout=5)

    def user_fill_form(self, email=None, password=None):
        if email is not None:
            self.email.send_keys(email)
        if password is not None:
            self.password.send_keys(password)

    def submit(self):
        self.sign_in.click()
        self.no_sign_in_disabled_element
