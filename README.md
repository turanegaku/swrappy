# swrappy
slack api wrapper get and post timeline

## Install
```bash
pip install git+git://github.com/turanegaku/swrappy.git
```

## Util
set your API TOKEN to `bots_config.json`
```json
{
  "botid1": {"TOKEN": "xxxx-xxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxx"},
  "botid2": {"TOKEN": "xxxx-xxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxx"}
}
```
#### Get History
```python
from swrappy import WebAPI

sl = WebAPI('bot')

h = sl.channels_history(channel='#general')
print(h)
```

#### WebAPI
```python
from swrappy import WebAPI

sl = WebAPI('bot')

sl.post_message(text='test', channel='#general')
```

#### RTMAPI
```python
from swrappy import RTMAPI

def on_message(message):
  print(message)

sl = RTMAPI('bot')
sl.on_message = on_message
sl.rtm_start()
```

### Help
if there is not config file on same dir with the script file,
```python
WebAPI.setConfigDir('./other/dir/')
sl = WebAPI('bot')
```
