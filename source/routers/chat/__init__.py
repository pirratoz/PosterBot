__all__ = [
    "router_chat",
]

from aiogram import (
    Router,
    F,
)

from source.routers.chat.create_remove_chat import create_remove_chat

router_chat = Router(name="chat")

router_chat.message.register(
    create_remove_chat,
    (F.text == "/chat")
)
