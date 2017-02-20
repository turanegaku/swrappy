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
  "botid1": {"TOKEN": 'xxxx-xxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxx'}
  "botid2": {"TOKEN": 'xxxx-xxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxx'}
}
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

sl = WebAPI('bot')

sl.post_message(text='test', channel='#general')
```

### Help
if there is not config file on same dir with the script file,
```python
WebAPI.setConfigDir('./other/dir/')
sl = WebAPI('bot')
```
