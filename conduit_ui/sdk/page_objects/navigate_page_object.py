from page_objects import PageObject, PageElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class NavigateConduitPageObject(PageObject):
    home = PageElement(link_text="Home")
    sign_in = PageElement(link_text="Sign in")
    sign_up = PageElement(link_text="Sign up")

    new_post = PageElement(link_text="New Post")
    settings = PageElement(link_text="Settings")

    def user_navigate_to_sign_in_page(self):
        self.sign_in.click()

    def user_navigate_to_sign_up_page(self):
        self.sign_up.click()

    def user_navigate_to_new_post_page(self):
        self.new_post.click()

    def user_is_logged_in(self):
        if not self.new_post:
            return False
        elif not self.settings:
            return False
        else:
            return True


class PageElementNotFound(PageElement):

    def __init__(self, context=False, timeout=5, **kwargs):
        super().__init__(context, **kwargs)
        self.timeout = timeout

    def find(self, context):
        WebDriverWait(context, self.timeout).until(EC.invisibility_of_element_located(self.locator))