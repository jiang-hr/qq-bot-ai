from nonebot import on_command
from nonebot.plugin import on_regex
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
import json
import urllib
import urllib.request
import re
from urllib.parse import urlencode

a = "(\\d|\\.){1,}\\s*(((u|U)(s|S)(d|D))|(J|j)(P|p)(Y|y)|(E|e)(U|u)(R|r)" +\
    "|(G|g)(B|b)(P|p)|(S|s)(U|u)(R|r)|(C|c)(A|a)(D|d)|(F|f)(R|r)(F|f)" +\
    "|(H|h)(K|k)(D|d)|(C|c)(H|h)(F|g)|(D|d)(E|e)(M|m)|(A|a)(U|u)(D|d)" +\
    "|(S|s)(G|g)(D|d))"
weather = on_regex(a, rule=None, priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["rate"] = re.match(a, args).group()  # 如果用户发送了参数则直接赋值


@weather.got("rate", prompt="你想查询哪个城市的天气呢？")
async def handle_rate(bot: Bot, event: Event, state: dict):
    rate = state["rate"]
    money = float(rate[:-3])
    place = rate[-3:].upper()
    print(money)
    print(place)
    params = {
        'app': 'finance.rate',
        'scur': place,
        'tcur': 'CNY',
        'appkey': '55767',
        'sign': 'e42fc54147bdbada67f25bc83540d1ab',
        'format': 'json',
    }
    params = urlencode(params)
    url = 'http://api.k780.com'
    f = urllib.request.urlopen('%s?%s' % (url, params))
    nowapi_call = f.read()

    a_result = json.loads(nowapi_call)
    if a_result:
        pass
    else:
        await weather.finish('Request nowapi fail. 请等1小时后再调用')
    print(a_result['result'])
    m = a_result['result']
    be_sent = str(float(m["rate"]) * money) + \
        " CNY\n更新自： " + m["update"]

    await weather.finish(be_sent)
