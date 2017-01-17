def delete_histories(sl, histories, channel, user=None, text=None):
    if user:
        histories = [h for h in histories if 'user' in h and h['user'] is user]
    if text:
        histories = [h for h in histories if 'text' in h and h['text'] is text]
    if channel.startswith('#'):
        channels = sl.channels_list()
        channel = [c for c in channels if 'name' in c and c['name'] is channel[1:]][0]['id']

    for h in histories:
        sl.chat_delete(ts=h['ts'], channel=channel)
