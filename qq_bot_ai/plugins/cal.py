from nonebot import on_command
from nonebot.plugin import on_regex
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from sympy import *
from time import localtime as now
import re
from base64 import *
from libnum import *
from random import *

calculator = on_regex(".*", rule=None, priority=1000)


@calculator.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message)
    print(args)
    if args:
        state["string"] = args  # 如果用户发送了参数则直接赋值
    temp_state_str = state["string"]
    des = "\"请勿破坏蓝的算力\""
    forbid = "\"这句话不被允许执行\""
    priva = "\"不允许访问这里\""
    a = False
    stop = False
    try:
        temp = float(state["string"])
        stop = True
    except ValueError:
        pass
    if re.match("\\s*\".*\"\\s*", state["string"]) and state["string"].count("\"") == 2:
        a = True
    if re.match("\\s*\'.*\'\\s*", state["string"]) and state["string"].count("\'") == 2:
        a = True
    if len(state["string"]) > 200:
        stop = True
    cnt = state["string"].count("*") + 2 * state["string"].count("integrate") +\
        state["string"].count("sin")+state["string"].count("cos") +\
        3 * state["string"].count("limit") + 2*state["string"].count("gamma") +\
        state["string"].count("tan") + state["string"].count("diff") +\
        state["string"].count("**") + 2 * state["string"].count("exp")
    if cnt > 12:
        state["string"] = forbid
    if re.match(".*__.*__", state["string"]):
        stop = True
    if re.match(".*os\\s*\\.", state["string"]):
        stop = True
    if re.match(".*(to_me|Bot|Event|on_command|nonebot)", state["string"]):
        stop = True
    if re.match(".*sleep", state["string"]):
        stop = True
    if re.match(".*(integrate|exp|gamma)\\s*\\(\\s*\\d{4,}", state["string"]):
        stop = True
    if re.match(".*(integrate|exp|gamma)\\s*\\(.*\\s*\\d{1,}\\s*\\*+\\s*\\d{1,}", state["string"]):
        stop = True
    if re.match(".*dir\\s*\\(\\s*\\)", state["string"]):
        state["string"] = priva
    if re.match(".*\\*\\*\\s*gamma", state["string"]):
        stop = True
    if re.match(".*(integrate|exp|gamma).*\\*\\*\\s*\\d{2,}", state["string"]):
        stop = True
    if re.match(".*(range|help|main|read|open|import|exec|for\\s|while|eval\\s*\\()", state["string"]):
        stop = True
    if re.match(".*\\*\\*\\s*\\d+\\s*\\*\\*\\s*\\d+", state["string"]):
        stop = True
    if re.match(".*\\*\\*\\s*\\d{4,}", state["string"]):
        stop = True
    if re.match(".*\\s*\\d{2,}\\s*\\*\\*\\s*\\d{2,}", state["string"]):
        state["string"] = des
    if state["string"].find("\n") >= 0:
        stop = True
    if a == True:
        state["string"] = temp_state_str
    if stop:
        state["string"] = ""


def cal(state: dict):
    x = Symbol("x")
    y = Symbol("y")
    z = Symbol("z")
    n = Symbol("n")
    m = Symbol("m")
    f = Function("f")
    g = Function("g")
    e = E
    umi = rbq = "rbq"
    真红 = "真红"
    ntr = "爬"
    贴贴 = "贴贴"
    string = state["string"]
    if string == "":
        return ""
    try:
        string_calculator = str(eval(string))
    except BaseException as e:
        string_calculator = ""
    if len(string_calculator) > 500:
        string_calculator = string_calculator[:500] + '...更多省略'
    return string_calculator


@calculator.got("string", prompt=" ")
async def handle_string(bot: Bot, event: Event, state: dict):
    string_calculator = cal(state)
    if string_calculator == "":
        await calculator.finish()
    await calculator.finish(string_calculator)
