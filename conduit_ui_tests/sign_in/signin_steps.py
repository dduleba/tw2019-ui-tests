from radish import steps, after
from radish_selenium.radish.selenium_base_steps import attach_screenshot_on_failure, \
    attach_page_source_on_failure, attach_console_log_on_failure, close_web_browser

# from realworld_ui.sdk.page_objects.general import LoggedPageObject
from conduit_rest.radish.conduit_rest_steps import ConduitRestBaseSteps
from conduit_ui.radish.ui_steps import ConduitBaseSteps, SignInBaseSteps


@after.each_step
def on_failure(step):
    attach_screenshot_on_failure(step)
    attach_page_source_on_failure(step)
    attach_console_log_on_failure(step)

@after.each_scenario
def test_cleanup(scenario):
    close_web_browser(scenario)

@steps
class ConduitSteps(ConduitBaseSteps):
    pass


@steps
class ConduitRestSteps(ConduitRestBaseSteps):
    pass


@steps
class SignInSteps(SignInBaseSteps):
    pass
