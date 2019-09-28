from faker import Faker
from nose.tools import assert_true
from radish_selenium.radish.selenium_base_steps import open_web_browser
from radish_selenium.radish.selenium_steps_config import get_selenium_config

from conduit_rest.radish.conduit_rest_steps import get_conduit_config
from conduit_ui.sdk.page_objects.article_page_obejct import CreateArticlePageObject, ViewArticlePageObject
from conduit_ui.sdk.page_objects.navigate_page_object import NavigateConduitPageObject
from conduit_ui.sdk.page_objects.signin_page_object import SignInPageObject


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
        NavigateConduitPageObject(stc.driver).user_navigate_to_sign_up_page()

    def user_navigate_to_sign_in_page(self, step):
        """User navigate to Sign in page"""
        stc = get_selenium_config(step.context)
        NavigateConduitPageObject(stc.driver).user_navigate_to_sign_in_page()

    def user_navigate_to_new_post_page(self, step):
        """User navigate to create article page"""
        stc = get_selenium_config(step.context)
        NavigateConduitPageObject(stc.driver).user_navigate_to_new_post_page()

    def user_should_be_logged_in(self, step):
        """User should be logged in"""
        stc = get_selenium_config(step.context)
        lp = NavigateConduitPageObject(stc.driver)
        assert_true(lp.user_is_logged_in(), "User should be logged in")
    #     stc.attach_screenshot_to_tests_report(step)


class SignInBaseSteps(object):
    def user_is_signed_in(self, step):
        """User is signed in"""
        stc = get_selenium_config(step.context)
        stc_conduit = get_conduit_config(step.context)
        ConduitBaseSteps().user_navigate_to_sign_in_page(step)
        user_model = stc_conduit.test_data.data.get('user')
        sign_in_page = SignInPageObject(stc.driver)
        sign_in_page.user_fill_form(user_model.get('email'), user_model.get('password'))
        sign_in_page.submit()


class ArticleBaseSteps(object):
    def user_fills_the_new_article_form(self, step, ):
        """User fills the new article form"""
        stc = get_selenium_config(step.context)
        art = CreateArticlePageObject(stc.driver)
        f = Faker()
        text = f.text()
        words = text.split()
        title = f.sentence(ext_word_list=words, nb_words=3)
        about = f.sentence(ext_word_list=words, nb_words=5)
        # tag = f.word(ext_word_list=words)
        article = {
            'article': text,
            'title': title,
            # 'tag': tag,
            'about': about,
        }
        art.user_fill_form(article)
        stc.attach_screenshot_to_tests_report(step)

    def user_sumbit_the_new_article_form(self, step, ):
        """User sumbit the new article form"""
        stc = get_selenium_config(step.context)
        art = CreateArticlePageObject(stc.driver)
        art.submit()

    def user_should_see_the_new_article_on_page(self, step, ):
        """User should see the new article on page"""
        stc = get_selenium_config(step.context)
        art = ViewArticlePageObject(stc.driver)
        stc.log.info(art.read_title())
        stc.log.info(art.read_article())
