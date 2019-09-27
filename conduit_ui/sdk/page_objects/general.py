from nose.tools import assert_is_not_none
from page_objects import PageObject, PageElement


class BaseConduitPageObject(PageObject):

    home = PageElement(link_text="Home")
    sign_in = PageElement(link_text="Sign in")
    sign_up = PageElement(link_text="Sign up")

    new_post = PageElement(link_text="New Post")
    settings = PageElement(link_text="Settings")

    def user_navigate_to_sign_in_page(self):
        self.sign_in.click()

    def user_navigate_to_sign_up_page(self):
        self.sign_up.click()

    def user_is_logged_in(self):
        if not self.new_post:
            return False
        elif not self.settings:
            return False
        else:
            return True