from page_objects import PageObject, PageElement

from conduit_ui.sdk.page_objects.navigate_page_object import PageElementNotFound


class SignupPageObject(PageObject):
    username = PageElement(xpath='//input[@placeholder="Username"]')
    email = PageElement(xpath='//input[@placeholder="Email"]')
    password = PageElement(xpath='//input[@placeholder="Password"]')
    sign_up = PageElement(xpath='//button[text()="Sign up"]')
    no_sign_up_disabled_element = PageElementNotFound(xpath='//button[text()="Sign up" and @disabled]', timeout=5)

    def user_fill_form(self, username=None, email=None, password=None):
        if username is not None:
            self.username.send_keys(username)
        if email is not None:
            self.email.send_keys(email)
        if password is not None:
            self.password.send_keys(password)

    def submit(self):
        self.sign_up.click()
        self.no_sign_up_disabled_element
