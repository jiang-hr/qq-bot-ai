from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from sympy import *
from time import localtime as now
import re

calculator = on_command("cal", rule=None, priority=1)


@calculator.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message)
    print(args)
    if args:
        state["string"] = args  # 如果用户发送了参数则直接赋值
    temp_state_str = state["string"]
    err = "\"请勿使用危险方法尝试破坏蓝\""
    des = "\"请勿破坏蓝的算力\""
    forbid = "\"这句话不被允许执行\""
    a = False
    if re.match("\\s*\".*\"\\s*", state["string"]) and state["string"].count("\"") == 2:
        a = True
    if re.match("\\s*\'.*\'\\s*", state["string"]) and state["string"].count("\'") == 2:
        a = True
    if len(state["string"]) > 200:
        state["string"] = "\"请重新输入\""
    if re.match(".*os\\s*\\.", state["string"]):
        state["string"] = err
    if re.match(".*nonebot", state["string"]):
        state["string"] = forbid
    if re.match(".*sleep", state["string"]):
        state["string"] = forbid
    if re.match(".*gamma\\s*\\(\\s*\\d{4,}", state["string"]):
        state["string"] = forbid
    if re.match(".*gamma\\s*\\(.*\\s*\\d{1,}\\s*\\**\\s*\\d{1,}", state["string"]):
        state["string"] = forbid
    if re.match(".*dir\\s*\\(\\s*\\)", state["string"]):
        state["string"] = forbid
    if state["string"].find("help") >= 0:
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
    if a == True:
        state["string"] = temp_state_str


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
    if len(string_calculator) > 500:
        string_calculator = string_calculator[:500] + '...更多省略'
    return string_calculator


@calculator.got("string", prompt=" ")
async def handle_string(bot: Bot, event: Event, state: dict):
    string_calculator = cal(state)
    await calculator.finish(string_calculator)
