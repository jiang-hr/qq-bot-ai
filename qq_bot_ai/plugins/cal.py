from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from sympy import *
from time import localtime as now
import re
from base64 import *
from libnum import *
from random import *

calculator = on_command("cal", rule=None, priority=1)



@calculator.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message)
    print(args)
    if args:
        state["string"] = args  # 如果用户发送了参数则直接赋值
    temp_state_str = state["string"]
    err = "\"请勿尝试使用可能破坏蓝的危险方法\""
    des = "\"请勿破坏蓝的算力\""
    forbid = "\"这句话不被允许执行\""
    priva = "\"不允许访问这里\""
    a = False
    if re.match("\\s*\".*\"\\s*", state["string"]) and state["string"].count("\"") == 2:
        a = True
    if re.match("\\s*\'.*\'\\s*", state["string"]) and state["string"].count("\'") == 2:
        a = True
    cnt = state["string"].count("*") + 2 * state["string"].count("integrate") +\
        state["string"].count("sin")+state["string"].count("cos") +\
        3 * state["string"].count("limit") + 2*state["string"].count("gamma") +\
        state["string"].count("tan") + state["string"].count("diff") +\
        state["string"].count("**") + 2 * state["string"].count("exp")
    if cnt > 12:
        state["string"] = forbid
    if len(state["string"]) > 200:
        state["string"] = "\"请重新输入\""
    if re.match(".*__.*__", state["string"]):
        state["string"] = "\"不允许使用魔法方法\""
    if re.match(".*os\\s*\\.", state["string"]):
        state["string"] = err
    if re.match(".*(to_me|Bot|Event|on_command|nonebot)", state["string"]):
        state["string"] = priva
    if re.match(".*sleep", state["string"]):
        state["string"] = forbid
    if re.match(".*gamma\\s*\\(\\s*\\d{4,}", state["string"]):
        state["string"] = forbid
    if re.match(".*gamma\\s*\\(.*\\s*\\d{1,}\\s*\\*+\\s*\\d{1,}", state["string"]):
        state["string"] = forbid
    if re.match(".*dir\\s*\\(\\s*\\)", state["string"]):
        state["string"] = priva
    if re.match(".*\\*\\*\\s*gamma", state["string"]):
        state["string"] = forbid
    if re.match(".*integrate.*\\*\\*\\s*\\d{2,}", state["string"]):
        state["string"] = forbid
    if re.match(".*(help|main|read|open|import|exec)", state["string"]):
        state["string"] = err
    if re.match(".*eval(\\s*\\()", state["string"]):
        state["string"] = err
    if re.match(".*for\\s", state["string"]):
        state["string"] = des
    if re.match(".*while", state["string"]):
        state["string"] = des
    if state["string"].find("range") >= 0:
        state["string"] = des
    if re.match(".*\\*\\*\\s*\\d+\\s*\\*\\*\\s*\\d+", state["string"]):
        state["string"] = forbid
    if re.match(".*\\*\\*\\s\\d{4,}", state["string"]):
        state["string"] = des
    if re.match(".*\\s*\\d{2,}\\s*\\*\\*\\s*\\d{3,}", state["string"]):
        state["string"] = des
    if state["string"].find("\n") >= 0:
        state["string"] = "\"请勿尝试换行\""
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
    真红 = "真红"
    透 = "透"
    喜欢 = "我永远喜欢"
    ntr = "爬"
    伊卡 = "rbq"
    string = state["string"]
    try:
        string_calculator = str(eval(string))
    except BaseException as e:
        string_calculator = "蓝执行出现错误，错误原因如下：\n" + str(e.args)
    if len(string_calculator) > 500:
        string_calculator = string_calculator[:500] + '...更多省略'
    return string_calculator


@calculator.got("string", prompt=" ")
async def handle_string(bot: Bot, event: Event, state: dict):
    string_calculator = cal(state)
    await calculator.finish(string_calculator)
