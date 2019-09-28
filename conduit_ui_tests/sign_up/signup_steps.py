from faker import Faker
from radish import steps, after
from radish_selenium.radish.selenium_base_steps import SeleniumBaseSteps, attach_screenshot_on_failure, \
    attach_page_source_on_failure, attach_console_log_on_failure
from radish_selenium.radish.selenium_steps_config import get_selenium_config

# from realworld_ui.sdk.page_objects.general import LoggedPageObject
from conduit_rest.radish.conduit_rest_steps import get_conduit_config
from conduit_ui.radish.ui_steps import ConduitBaseSteps
from conduit_ui.sdk.page_objects.signup_page_object import SignupPageObject


@after.each_step
def on_failure(step):
    attach_screenshot_on_failure(step)
    attach_page_source_on_failure(step)
    attach_console_log_on_failure(step)


@steps
class SeleniumSteps(SeleniumBaseSteps):
    pass


@steps
class SignupSteps(object):

    def user_fills_the_sign_up_page(self, step):
        """User fills the Sign up page"""
        stc = get_selenium_config(step.context)
        stc_conduit = get_conduit_config(step.context)
        spo = SignupPageObject(stc.driver)
        faker_ = stc_conduit.faker
        username = faker_.user_name()
        userpass = faker_.password()
        useremail = faker_.email()
        spo.user_fill_form(username, useremail, userpass)

    def user_enter_username(self, step, username):
        """User enter username {username:QuotedString}"""
        stc = get_selenium_config(step.context)
        spo = SignupPageObject(stc.driver)
        spo.user_fill_form(username=username)

    def user_enter_email(self, step, email):
        """User enter email {email:QuotedString}"""
        stc = get_selenium_config(step.context)
        spo = SignupPageObject(stc.driver)
        spo.user_fill_form(email=email)

    def user_enter_password(self, step, password):
        """User enter password {password:QuotedString}"""
        stc = get_selenium_config(step.context)
        spo = SignupPageObject(stc.driver)
        spo.user_fill_form(password=password)

    def user_submit_form(self, step):
        """User submit the Sign up page"""
        stc = get_selenium_config(step.context)
        rp = SignupPageObject(stc.driver)
        rp.submit()
        stc.attach_screenshot_to_tests_report(step)


@steps
class ConduitSteps(ConduitBaseSteps):
    pass
