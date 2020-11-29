from nonebot.plugin import on_regex
from nonebot.adapters.cqhttp import Bot, Event

vpn_warn = on_regex(".*((V|v)(P|p)(N|n)|ssr|v2ray|(T|t)rojan|(T|t)or|(G|g)(W|w)(F|f))",
                   rule=None, priority=8)


@vpn_warn.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    state["vpn"] = "蓝的警告：使用非法信道与外网通讯违法，请勿以身试法⚠"


@vpn_warn.got("vpn", prompt=None)
async def handle_vpn(bot: Bot, event: Event, state: dict):
    vpn = state["vpn"]
    await vpn_warn.finish(vpn)
