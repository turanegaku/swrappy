def delete_histories(sl, histories, channel, user=None, text=None):
    if user:
        histories = [h for h in histories if 'user' in h and h['user'] is user]
    if text:
        histories = [h for h in histories if 'text' in h and h['text'] is text]
    if channel.startswith('#'):
        channel = find_channel(sl, channel)['id']

    for h in histories:
        sl.chat_delete(ts=h['ts'], channel=channel)

def find_channel(sl, name, force_load=False):
    if not sl.channels or force_load:
        sl.channels = sl.channels_list()

    channels = [c for c in sl.channels if 'name' in c and c['name'] == name[1:]]
    return channels[0] if channels else None
