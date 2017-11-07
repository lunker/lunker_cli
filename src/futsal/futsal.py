from crawl.crawler import NaverCrawler
from util.slack import SlackHelper


class FutsalFinder:

    def __init__(self):
        self.cralwer = NaverCrawler()
        self.slack = SlackHelper()
        pass

    def search_latest_matching(self):

        user_id = input("Enter id: ")
        user_pwd = input("Enter password: ")

        self.cralwer.login(user_id, user_pwd)
        article_list = self.cralwer.gather_latest_matching_article()

        if article_list is not None:
            for article in article_list:
                slack_message = self.slack.create_message(article)
                self.slack.send_message(slack_message)
        else:
            # Error!
            pass