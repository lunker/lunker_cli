import websocket, ssl, json
import asyncio
from util.singleton import Singleton


class WebsocketHandler(Singleton):

    def __init__(self, url):
        self.ws = None
        self.callback = None
        self.endpoint = url

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        asyncio.get_event_loop().run_until_complete(self.connect())
        asyncio.get_event_loop().run_forever()

        pass

    def add_message_handler(self, callback):
        self.callback = callback

    async def connect(self):
        print("start slack server...")

        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.endpoint, on_message=self.__on_message(), on_open=self.__on_open())
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    def __on_open(self, *args):
        print("Open Websocket Client")

    def __on_message(self, *args):
        print(args)
        json_response = json.loads(args[1])
        if 'type' in json_response and json_response['type'] == 'message':
            print(json_response['text'])
            message = {'id': 1, 'type': 'message', 'channel': json_response['channel'], 'text': 'wow!'}
            # self.ws.send(json.dumps(message))
            if self.callback is None:
                # Raise NoCallbackError
                print("NoCallbackError!")
            else:
                self.callback(json.dumps(message))

    def get_websocket_handler(self):
        return self.ws