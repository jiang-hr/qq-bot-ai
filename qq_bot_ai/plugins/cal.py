from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from sympy import *
import time
import re

calculator = on_command("cal", rule=None, priority=1)


@calculator.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message)
    print(args)
    err = "\"请勿使用危险方法破坏蓝\""
    des = "\"请勿破坏蓝的算力\""
    if args:
        state["string"] = args  # 如果用户发送了参数则直接赋值
    if len(state["string"]) > 30:
        state["string"] = "\"请重新输入\""
    if re.match(".*os\\s*\\.", state["string"]):
        state["string"] = err
    if state["string"].find("read") >= 0:
        state["string"] = err
    if state["string"].find("open") >= 0:
        state["string"] = err
    if state["string"].find("eval") >= 0:
        state["string"] = err
    if state["string"].find("import") >= 0:
        state["string"] = err
    if state["string"].find("from") >= 0:
        state["string"] = err
    if state["string"].find("exec") >= 0:
        state["string"] = err
    if state["string"].find("for") >= 0:
        state["string"] = des
    if state["string"].find("while") >= 0:
        state["string"] = des
    if state["string"].find("range") >= 0:
        state["string"] = des
    if re.match(".*\\*\\*\\s*\\d+\\s*\\*\\*\\s*\\d+", state["string"]):
        state["string"] = des
    if re.match(".*\\*\\*\\s\\d{4,}", state["string"]):
        state["string"] = des
    if re.match(".*\\s*\\d{2,}\\s*\\*\\*\\s*\\d{3,}", state["string"]):
        state["string"] = des
    if state["string"].find("\n") >= 0:
        state["string"] = "\"请勿换行\""


def cal(state: dict):
    x = Symbol("x")
    y = Symbol("y")
    z = Symbol("z")
    n = Symbol("n")
    m = Symbol("m")
    f = Function("f")
    g = Function("g")
    e = E
    umi = "rbq"
    rbq = "rbq"
    伊卡 = "rbq"
    真红 = "真红"
    string = state["string"]
    string_calculator = str(eval(string))
    return string_calculator


@calculator.got("string", prompt=" ")
async def handle_string(bot: Bot, event: Event, state: dict):
    string_calculator = cal(state)
    await calculator.finish(string_calculator)
