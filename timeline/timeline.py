""" module for connect to TimeLine """
import requests

URL = 'https://slack.com/api/'

class timeline:
    def __init__(self, TOKEN):
        self.TOKEN = TOKEN


    def request(self, api, data=None, files=None, channel=None):
        """ set final parameters and send requests """
        if not data:
            data = dict()

        data['channel'] = channel if channel else '#bot'
        data['token'] = self.TOKEN

        return requests.post(URL + api, data=data, files=files)


    def post(self, text, data=None, channel=None):
        """ post text message """
        if not data:
            data = dict()
        data['text'] = text
        return request(api='chat.postMessage', data=data, channel=channel)


    def postfile(self, filepath, data=None, channel=None):
        """ post file message """
        with open(filepath, 'rb') as file:
            # 'initial_comment': comment,

            return request(api='files.upload', data=data, files={'file': file}, channel=channel)
