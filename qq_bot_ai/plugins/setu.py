from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment

weather = on_command("色图", rule=None, priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message)
    if args:
        state["city"] = args
    else:
        state["city"] = " "


@weather.got("city", prompt="")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await get_weather(city)
    a = MessageSegment.image("http://175.24.95.94/")
    print(a)
    await weather.finish(a)


async def get_weather(city: str):
    return f"{city}的天气是..."
