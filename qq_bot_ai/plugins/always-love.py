from nonebot import on_command, on_regex
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment
import random

I_always_love = on_regex("我永远喜欢", rule=None, priority=8)


@I_always_love.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    if args.find("我永远喜欢") == 0 and random.randint(0, 2) < 1:
        args = "我永远喜欢真红"
    if args:
        state["love"] = args
    else:
        state["love"] = " "


@I_always_love.got("love", prompt="")
async def handle_love(bot: Bot, event: Event, state: dict):
    if state["love"].find("真红") >= 0:
        await I_always_love.finish("我永远喜欢二阶堂真红")
    if state["love"].find("二阶堂蓝") >= 0:
        await I_always_love.finish("我永远喜欢二阶堂真红")
    elif random.randint(0, 1) < 1:
        await I_always_love.finish(state["love"])
    else:
        await I_always_love.finish()
