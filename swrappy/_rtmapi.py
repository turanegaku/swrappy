from swrappy._webapi import WebAPI
from ws4py.client.threadedclient import WebSocketClient

class RTMAPI(WebAPI):
    def __init__(self, name):
        super().__init__(name)

    def rtm_start(self):
        r = self.request('rtm.start')
        ws = WebSocketClient(r['url'])
        ws.received_message = self.received_message
        ws.opend = self.opened
        ws.closed = self.closed
        ws.connect()
        try:
            ws.run_forever()
        except KeyboardInterrupt:
            ws.close()

    def opened(self):
        print('open')

    def closed(self, code, reason):
        print('close')

    def received_message(self, m):
        message = json.loads(str(m))
        if message['type'] == 'message':
            self.on_message(message)
        elif message['type'] in ['reconnect_url', 'presence_change']:
            return
        print(m)

    def on_message(self, message):
        print(message)


if __name__ == '__main__':
    RTMAPI('imbot')
