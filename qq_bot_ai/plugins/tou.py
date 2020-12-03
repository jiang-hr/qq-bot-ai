from re import L
from nonebot import on_command
from nonebot.plugin import on_regex
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
import re

tou = on_regex("透", rule=None, priority=10)


@tou.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    stop = ""
    args = str(event.message)
    print(args)
    if args[0] != "透":
        args = stop
    args = args[1:]
    if len(args) <= 1:
        args = stop
    if args.find("透") >= 0:
        args = stop
    if args.find("\n") >= 0:
        args = stop
    state["bei_tou_people"] = args


@tou.got("bei_tou_people", prompt="")
async def handle_bei_tou_people(bot: Bot, event: Event, state: dict):
    bei_tou_people = state["bei_tou_people"]

    tou_people = await get_weather(bei_tou_people)
    print(bei_tou_people)
    if state["bei_tou_people"] == "":
        await tou.finish()
    if shield_shinnku(bei_tou_people):
        tou_people = "不要总是想方设法的透真红妹妹！"
    if re.match(".*蓝", bei_tou_people):
        tou.finish()
    await tou.finish(tou_people)


async def get_weather(bei_tou_people: str):
    return f"{bei_tou_people}，透！"


def shield_shinnku(string: str):
    answer = False
    if len(string) == 1:
        return False
    a = ".*(((r|R)(E|e)(A|a)(L|l|I)|(T|t|т)(R|r)(U|u)(E|e)|真|(s|S)(h|н|H)(i|Ï)|针|珍|zhen|眞|帧|不.*假|稹|蒖)|((s|S)(h|н|H)(i|Ï|I)|し|シ).*((n|N)*|ん|シ)).*((红|虹|紅|red|Red|(纟.*工)|洪|宏|荭)|((K|k|к)(U|u)|く|ク))"
    if (re.match(a, string)):
        answer = True
    if string.find("1062311924") >= 0:
        answer = True
    return answer
