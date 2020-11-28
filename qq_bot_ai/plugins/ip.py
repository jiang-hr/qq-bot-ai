from nonebot import on_command
from nonebot.plugin import on_regex
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
import json
import urllib
import urllib.request
import re
from urllib.parse import urlencode

a = "^([1-9]?\\d|1\\d{2}|2[0-4]\\d|25[0-5])(\\.([1-9]?\\d|1\\d{2}|2[0-4]\\d|25[0-5])){3}$"
weather = on_regex(a, rule=None, priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    state["rate"] = args  # 如果用户发送了参数则直接赋值


@weather.got("rate", prompt="")
async def handle_rate(bot: Bot, event: Event, state: dict):
    rate = state["rate"]
    params = {
        'app': 'ip.get',
        'ip': rate,
        'appkey': '55767',
        'sign': 'e42fc54147bdbada67f25bc83540d1ab',
        'format': 'json',
    }
    params = urlencode(params)
    url = 'http://api.k780.com'
    f = urllib.request.urlopen('%s?%s' % (url, params))
    nowapi_call = f.read()

    a_result = json.loads(nowapi_call)
    if not a_result:
        await weather.finish('Request nowapi fail. 请等1小时后再调用')
    print(a_result['result'])
    m = a_result['result']
    await weather.finish(m["detailed"])
