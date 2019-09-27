from nose.tools import assert_true
from radish import steps
from radish_selenium.radish.selenium_base_steps import open_web_browser
from radish_selenium.radish.selenium_steps_config import get_selenium_config

from conduit_ui.sdk.page_objects.general import BaseConduitPageObject


class ConduitBaseSteps(object):

    def conduit_page_is_opened(self, step):
        """conduit page is opened"""
        self.user_opens_conduit_page(step)

    def user_opens_conduit_page(self, step):
        """User opens conduit page"""
        stc = get_selenium_config(step.context)
        open_web_browser(step)
        stc.driver.get(stc.cfg['conduit_frontend']['url'])

    def user_navigate_to_sign_up_page(self, step):
        """User navigate to Sign up page"""
        stc = get_selenium_config(step.context)
        BaseConduitPageObject(stc.driver).user_navigate_to_sign_up_page()

    def user_should_be_logged_in(self, step):
        """User should be logged in"""
        stc = get_selenium_config(step.context)
        lp = BaseConduitPageObject(stc.driver)
        assert_true(lp.user_is_logged_in(), "User should be logged in")
    #     stc.attach_screenshot_to_tests_report(step)