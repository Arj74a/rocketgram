# Rocketgram

![TEST](https:/rosetech786/github.com//rocketgram/workflows/TEST/badge.svg)

Modern and powerful asynchronous telegram bot framework.

Release news available here: [@RocketgramNews](https://t.me/RocketgramNews)

## Dependencies

All dependencies are optional, but you should install `aiohttp` to use the framework.

`orjson` or `ujson` is highly recommended to speedup json parsing.

Also, you can use `uvloop` as alternative to standard event loop.

* Python >= 3.7
* aiohttp >= 3.8.1
* ujson >= 5.2.0
* orjson >= 3.6.8
* uvloop >= 0.12.1

## How to install

#### For development

```bash
pip install rocketgram[aiohttp]
```

#### For production

```bash
pip install uvloop rocketgram[aiohttp,orjson]
```

## Example

There is a trivial example below.
[Here](https://github.com/vd2org/rocketgram-template) is useful bot template.

```python
from rocketgram import Bot, Dispatcher, UpdatesExecutor
from rocketgram import context, commonfilters
from rocketgram import SendMessage

token = f'YOUR_BOT_TOKEN'

router = Dispatcher()
bot = Bot(token, router=router)

@router.handler
@commonfilters.command('/start')
async def start_command():
    await SendMessage(context.user.id, f'Hello there!').send()
    
@router.handler
@commonfilters.command('/help')
async def start_command():
    await SendMessage(context.user.id, f'Some userful help!').send()
    
UpdatesExecutor.run(bot)
```

# Testing

Code tested automatically using `Github Actions`. 
You can see build status **[here](https://github.com/rocketgram/rocketgram/actions)**.

To test code manually install and run `pytest`:

```bash
pip install pytest
python -m pytest
```
