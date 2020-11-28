from nonebot.plugin import on_regex
from nonebot.adapters.cqhttp import Bot, Event

weather = on_regex(".*((V|v)(P|p)(N|n)|ssr|v2ray|(T|t)rojan)",
                   rule=None, priority=8)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    state["vpn"] = "蓝的警告：使用非法信道与外网通讯违法，请勿以身试法⚠"


@weather.got("vpn", prompt=None)
async def handle_vpn(bot: Bot, event: Event, state: dict):
    vpn = state["vpn"]
    await weather.finish(vpn)
