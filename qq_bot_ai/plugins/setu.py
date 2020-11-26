from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment
import time

weather = on_command("色图", rule=None, priority=2)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    if args:
        state["setu"] = args
    else:
        state["setu"] = ""


@weather.got("setu", prompt="")
async def handle_setu(bot: Bot, event: Event, state: dict):
    if (state["setu"] == "" or state["setu"] == " "):
        state["setu"] = 1
    setu = int(state["setu"])
    if setu <= 0:
        setu = 1
    if setu >= 5:
        setu = 5
    for i in range(setu):
        a = MessageSegment.image("https://api.mtyqx.cn/api/random.php")
        time.sleep(2)
        await weather.send(a)
        print(a)
    #a = MessageSegment.image("http://175.24.95.94/")
    await weather.finish()
