from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment

weather = on_command("涩图", rule=None, priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message)
    if args:
        state["setu"] = args
    else:
        state["setu"] = " "


@weather.got("setu", prompt="")
async def handle_setu(bot: Bot, event: Event, state: dict):
    setu = state["setu"]
    a = MessageSegment.image("https://api.mtyqx.cn/api/random.php")
    print(a)
    await weather.finish(a)
