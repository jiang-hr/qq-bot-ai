from re import L
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
import re

tou = on_command("透", rule=None, priority=5)


@tou.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    if args:
        state["bei_tou_people"] = args
    else:
        state["bei_tou_people"] = "umi🐎"


@tou.got("bei_tou_people", prompt="umi🐎，透！")
async def handle_bei_tou_people(bot: Bot, event: Event, state: dict):
    bei_tou_people = state["bei_tou_people"]

    tou_people = await get_weather(bei_tou_people)
    print(bei_tou_people)

    if shield_shinnku(bei_tou_people):
        tou_people = "不要总是想方设法的透真红妹妹！"
    if re.match("二阶堂蓝", bei_tou_people):
        tou_people = "蓝妹妹也不能透！"
    await tou.finish(tou_people)


async def get_weather(bei_tou_people: str):
    return f"{bei_tou_people}，透！"


def shield_shinnku(string: str):
    answer = False
    if len(string) == 1:
        return False
    zhen = False
    hong = False
    itr = 0
    itr = string.find("真")
    if itr >= 0:
        zhen = True
        itr = string.find("红", itr)
        if itr == -1:
            itr = string.find("紅")
            if itr >= 0:
                hong = True
            itr = string.find("纟")
            if itr >= 0:
                hong = True
        else:
            hong = True
    if zhen and hong:
        answer = True
    if string.find("1062311924") >= 0:
        answer = True
    shi = False
    nn = False
    ku = False
    if string.find("shi") >= 0 or string.find("Shi") >= 0 or string.find("し") >= 0 or string.find("シ") >= 0:
        shi = True
    if string.find("n") >= 0 or string.find("ん") >= 0 or string.find("シ") >= 0:
        nn = True
    if string.find("Ku") >= 0 or string.find("ku") >= 0 or string.find("く") >= 0 or string.find("ク") >= 0:
        ku = True
    if nn and shi and ku:
        answer = True
    return answer
