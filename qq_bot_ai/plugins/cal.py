from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from sympy import *
import time

calculator = on_command("cal", rule=None, priority=6)


@calculator.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message)
    print(args)
    if args:
        state["string"] = args  # 如果用户发送了参数则直接赋值
    if state["string"].find("eval") >= 0:
        state["string"] = "\"请勿使用危险方法\""
    if state["string"].find("\n") >= 0:
        state["string"] = "\"请勿换行\""


def cal(state: dict):
    x = Symbol("x")
    y = Symbol("y")
    z = Symbol("z")
    n = Symbol("n")
    m = Symbol("m")
    string = state["string"]
    string_calculator = str(eval(string))
    return string_calculator


@calculator.got("string", prompt="未检测到输入")
async def handle_string(bot: Bot, event: Event, state: dict):
    string_calculator = cal(state)
    await calculator.finish(string_calculator)


async def get_calculator(string: str):
    return f"{string}的天气是..."
