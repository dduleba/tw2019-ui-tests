from page_objects import PageElement
from radish_ext.sdk.l import Logging

from conduit_ui.sdk.page_objects.navigate_page_object import NavigateConduitPageObject, PageElementNotFound


class CreateArticlePageObject(NavigateConduitPageObject):
    article_title = PageElement(xpath='//input[@placeholder="Article Title"]')
    about = PageElement(xpath='//input[@placeholder="What\'s this article about?"]')
    tag = PageElement(xpath='//input[@placeholder="Enter tags"]')
    article = PageElement(xpath='//textarea[@placeholder="Write your article (in markdown)"]')
    publish_article = PageElement(xpath='//button[text()="Publish Article"]')
    no_publish_article_disabled_element = PageElementNotFound(xpath='//button[text()="Publish Article" and @disabled]',
                                                              timeout=10)

    def user_fill_form(self, article_model):
        self.log = Logging.get_object_logger(self)
        self.log.debug(article_model)
        if 'title' in article_model:
            self.article_title.send_keys(article_model.get('title'))
        if 'about' in article_model:
            self.about.send_keys(article_model.get('about'))
        if 'article' in article_model:
            self.article.send_keys(article_model.get('article'))
        if 'tag' in article_model:
            self.tag.send_keys(article_model.get('tag'))

    def submit(self):
        self.publish_article.click()
        self.no_publish_article_disabled_element


class ViewArticlePageObject(NavigateConduitPageObject):
    title = PageElement(xpath="//div[@class='container']/h1")
    article = PageElement(xpath="//div[contains(@class,'article-content')]//p")

    def read_title(self):
        return self.title.text

    def read_article(self):
        return self.article.text
