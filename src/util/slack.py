from slacker import Slacker
import ssl
import json
from crawl.article import NaverCafeArticleMetaData
from util.singleton import Singleton
from transport.websocket import WebsocketHandler


class SlackHelper(Singleton):

    __instance = None

    def __init__(self):
        # self.token = os.environ.get('SLACK_TOKEN')
        
        self.slack = Slacker(self.token)

        response = self.slack.rtm.start()
        self.endpoint = response.body['url']

        self.websocket_handler = WebsocketHandler(self.endpoint)

    def send_message(self, data):
        response = self.slack.chat.post_message('#futsal', text=None, attachments=data, as_user=True)
        return response

    def create_message(self, article):
        """
            Create decorated slack message
            
        :param article: 
        :type article: NaverCafeArticleMetaData
        :return: 
        """
        slack_message = dict()

        # TODO:
        # slack_message['pretext'] = article.title
        slack_message['title'] = article.title
        slack_message['title_link'] = article.url
        slack_message['fallback'] = "New Futsal Matching is found"
        slack_message['text'] = article.content

        slack_attachments = [slack_message]
        return slack_attachments


if __name__ == '__main__':
    slack = SlackHelper()
    pass