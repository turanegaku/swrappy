from os import path
import sys
import requests
import json

from swrappy._util import find_channel

URL = 'https://slack.com/api/'


class WebAPI(object):
    CONFIG_PATH = path.join(path.dirname(sys.argv[0]), 'bots_config.json')

    @staticmethod
    def setConfigDir(dir):
        WebAPI.CONFIG_PATH = path.join(path.abspath(dir), 'bots_config.json')
        return WebAPI.CONFIG_PATH

    def __init__(self, name):
        with open(WebAPI.CONFIG_PATH, 'r') as f:
            config = json.load(f)
        self.TOKEN = config[name]['TOKEN']

        self.channels = None

    def request(self, api, data=None, files=None):
        if not data:
            data = dict()

        data['token'] = self.TOKEN
        if 'username' not in data:
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

    def channels_history(self, channel, latest=None, oldest=None, count=None):
        if channel.startswith('#'):
            c = find_channel(self, channel)['id']
            if not c:
                return None
            channel = c

        data = {
                'channel': channel,
                'latest': latest,
                'oldest': oldest,
                'count': count,
                }
        return self.request('channels.history', data=data)['messages']

    def chat_delete(self, ts, channel):
        data = {
                'ts': ts,
                'channel': channel
                }
        return self.request('chat.delete', data=data)

    def post_message(self, text, channel, username=None, icon_emoji=None, attachments=None):
        """ post text message """
        data = {
                'text': text,
                'channel': channel,
                'attachments': attachments,
                }
        if username:
            data['username'] = username
        if icon_emoji:
            data['icon_emoji'] = icon_emoji
        return self.request(api='chat.postMessage', data=data)

    def files_upload(self, filepath, data=None, text=None, channel=None):
        if not data:
            data = dict()
        if text:
            data['initial_comment'] = text
        if channel:
            data['channels'] = [channel]

        with open(filepath, 'rb') as file:
            return self.request(api='files.upload', data=data, files={'file': file})

    def files_delete(self, file_id):
        data = {'file': file_id}

        return self.request(api='files.delete', data=data)

if __name__ == '__main__':
    pass
