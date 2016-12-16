from os import path
import sys
import requests
import json

URL = 'https://slack.com/api/'
CONFIG_PATH = path.join(path.dirname(sys.argv[0]), 'bots_config.json')


class WebAPI(object):
    def __init__(self, name):
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)
        self.TOKEN = config[name]['TOKEN']

    def request(self, api, data=None, files=None):
        if not data:
            data = dict()

        data['token'] = self.TOKEN
        if 'username' not in data
            data['as_user'] = True
        r = requests.post(URL + api, data=data, files=files)

        if r.status_code != 200:
            raise Exception('responce status is %s\n\t%s' % (r.status_code, r.text))
        d = r.json()
        if not d['ok']:
            raise Exception(r.text)

        return d

    def rtm_start(self):
        return self.request('rtm.start')

    def auth_test(self):
        return self.request('auth.test')

    def users_list(self):
        return self.request('users.list')['members']

    def channels_list(self):
        return self.request('channels.list')['channels']

    def groups_list(self):
        return self.request('groups.list')['groups']

    def post_message(self, text, channel=None):
        """ post text message """
        data = {
                'text': text,
                'channel': channel,
                }
        return self.request(api='chat.postMessage', data=data)

    def files_upload(self, filepath, data=None, text=None, channel=None):
        """ post file message """
        if not data:
            data = dict()
        if text:
            data['initial_comment'] = text
        if channel:
            data['channels'] = [channel]

        with open(filepath, 'rb') as file:
            return self.request(api='files.upload', data=data, files={'file': file})


if __name__ == '__main__':
    WebAPI('imbot')
