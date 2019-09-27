from page_objects import PageObject, PageElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class PageElementNotFound(PageElement):

    def __init__(self, context=False, timeout=5, **kwargs):
        super().__init__(context, **kwargs)
        self.timeout=timeout

    def find(self, context):
        WebDriverWait(context, self.timeout).until(EC.invisibility_of_element_located(self.locator))

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
