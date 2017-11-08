import os
from slacker import Slacker
# from slackclient import SlackClient
import ssl
import json

import time
from crawl.article import NaverCafeArticleMetaData
import websocket
import websockets
import asyncio
from util.singleton import Singleton


class SlackHelper(Singleton):

    __instance = None

    def __init__(self):
        # self.token = os.environ.get('SLACK_TOKEN')
        self.token = 'xoxb-268017423619-yucLeWqiH1A4Y21fMC9r8lPy'
        self.slack = Slacker(self.token)

        # TODO(lunker): asyncio 공부
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        asyncio.get_event_loop().run_until_complete(self.__recv())
        asyncio.get_event_loop().run_forever()

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

    async def __recv(self):
        print("start slack server...")

        response = self.slack.rtm.start()
        self.endpoint = response.body['url']

        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.endpoint, on_message=self.on_message)

        self.ws.on_open = self.on_open
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    def on_message(self, *args):
        print(args)
        json_response = json.loads(args[1])
        if 'type' in json_response and json_response['type'] == 'message':
            print(json_response['text'])
            message = {'id':1, 'type': 'message', 'channel': 'D7W0HCGKV', 'text': 'wow!'}
            self.ws.send(json.dumps(message))

    def on_open(self, *args):
        print("Open!!")
        print(args)


class Bot:

    def __init__(self):
        pass


if __name__ == '__main__':
    slack = SlackHelper()
    pass