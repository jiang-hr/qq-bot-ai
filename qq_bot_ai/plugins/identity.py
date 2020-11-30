from nonebot import on_command
from nonebot.plugin import on_regex
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
import json
import urllib
import urllib.request
import re
from urllib.parse import urlencode

weather = on_regex(
    "^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$|^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}([0-9]|X)$", rule=None, priority=9)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    state["identity"] = args


def get(identity):
    url = 'http://api.k780.com'
    params = {
        'app': 'idcard.get',
        'idcard': identity,
        'appkey': '55767',
        'sign': 'e42fc54147bdbada67f25bc83540d1ab',
        'format': 'json',
    }
    params = urlencode(params)
    f = urllib.request.urlopen('%s?%s' % (url, params))
    nowapi_call = f.read()
    a_result = json.loads(nowapi_call)
    if a_result and a_result['success'] != '0':
        print(a_result['result'])
        return a_result['result']
    else:
        return "蓝没有得到结果，也许并不存在这个人呢"


@weather.got("identity", prompt="")
async def handle_identity(bot: Bot, event: Event, state: dict):
    m = get(state["identity"])
    if m == "蓝没有得到结果，也许并不存在这个人呢":
        await weather.finish(m)
    said = state["identity"] + "\n"
    said += "出生日期: " + m['born'] + "\n"
    said += "性别: " + m['sex'] + "\n"
    said += "户籍: " + m['att'] + "\n"
    await weather.finish(said)
