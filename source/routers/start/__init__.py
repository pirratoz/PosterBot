__all__ = [
    "router_start",
]

from aiogram import Router, F

from source.routers.start.start_cmd import handle_start_cmd


router_start = Router(name="start")

router_start.message.register(
    handle_start_cmd,
    F.text.in_({"/start", "меню"})
)
