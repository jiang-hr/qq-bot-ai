from re import L
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
import re

tou = on_command("透", rule=None, priority=5)


@tou.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message)
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
    if len(string) == 1:
        return False
    zhen = False
    hong = False
    itr = 0
    for i in string:
        itr += 1
        if i == "真":
            zhen = True
            break
    for i in string[itr:]:
        if i == "红" or i == "紅":
            hong = True
            break

    for i in range(len(string)-1)[itr:]:
        if string[i] == "纟" and string[i+1] == "工":
            hong = True
            break

    if zhen and hong:
        return True
    shi = False
    nn = False
    ku = False
    for i in range(len(string)-2):
        if (string[i] == "s" or string[i] == "S") and string[i+1] == "h" and string[i+2] == "i":
            shi = True
            break
    for i in range(len(string))[1:]:
        if string[i] == "n" and string[i-1] == "i":
            nn = True
            break
    for i in range(len(string)-1):
        if (string[i] == "k" or string[i] == "K") and string[i+1] == "u":
            ku = True
            break
    for i in string:
        if i == "し":
            shi = True
            break
    for i in string:
        if i == "ん":
            nn = True
            break
    for i in string:
        if i == "く":
            ku = True
            break
    for i in string:
        if i == "シ":
            shi = True
            break
    for i in string:
        if i == "ン":
            nn = True
            break
    for i in string:
        if i == "ク":
            ku = True
            break
    if nn and shi and ku:
        return True
    if re.match("hinnku", string):
        return True
    if re.match("True|true", string):
        for i in string:
            if i == "d":
                return True
    return False
