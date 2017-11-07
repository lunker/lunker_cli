from slackclient import SlackClient
from slacker import Slacker
from crawl.article import NaverCafeArticleMetaData


class SlackHelper:

    def send_message(self, data):
        # token = 'xoxb-268214032229-jUml5WQlqPOYCSokgXQQpOQ6'
        token = 'xoxb-268017423619-WNkS47iUEbMvaSMGUgEzvQNF'
        slack = Slacker(token)

        response = slack.chat.post_message('#futsal', text=None, attachments=data, as_user=True)

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


class Bot:

    def __init__(self):
        pass

