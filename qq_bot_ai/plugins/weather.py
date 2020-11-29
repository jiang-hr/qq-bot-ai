from nonebot import on_command
from nonebot.plugin import on_regex
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
import json
import urllib
import urllib.request
import re
from urllib.parse import urlencode

weather = on_regex(".*天气$", rule=None, priority=9)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    state["city"] = args[:-2]
    if state["city"][-1] == "的":
        state["city"] = state["city"][:-1]


def get(city):
    url = 'http://api.k780.com'
    params = {
        'app': 'weather.today',
        'weaid': city,
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
        return "蓝没有得到结果，请检查输入或者等1小时后再调用"


@weather.got("city", prompt="")
async def handle_city(bot: Bot, event: Event, state: dict):
    m = get(state["city"])
    if m == "蓝没有得到结果，请检查输入或者等1小时后再调用":
        await weather.finish(m)
    said = "城市: " + m['citynm'] + "\n"
    said += "今日温度: " + m['temperature'] + "\n"
    said += "实时温度: " + m['temperature_curr'] + "\n"
    said += "风向: " + m['wind'] + "\n"
    said += "风力: " + m['winp'] + "\n"
    said += "今日天气: " + m['weather'] + "\n"
    said += "实时天气: " + m['weather_curr'] + "\n"
    said += "湿度: " + m['humidity']
    await weather.finish(said)
