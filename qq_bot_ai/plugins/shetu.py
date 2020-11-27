from nonebot import on_command, on_regex
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment

weather = on_regex("涩图", rule=None, priority=8)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    if args != "涩图":
        await weather.finish()
    if args:
        state["setu"] = args
    else:
        state["setu"] = " "


@weather.got("setu", prompt="")
async def handle_setu(bot: Bot, event: Event, state: dict):
    a = MessageSegment.image("https://api.mtyqx.cn/api/random.php")
    print(a)
    await weather.finish(a)
