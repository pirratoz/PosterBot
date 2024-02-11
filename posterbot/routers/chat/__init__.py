__all__ = [
    "router_chat",
]

from aiogram import Router

from posterbot.routers.chat.handle_chat import handle_chat

from posterbot.utils.filters import ChatFilter


router_chat = Router("chat")


router_chat.message.register(
    handle_chat,
    *ChatFilter.APPEND_OR_REMOVE_CHAT()
)
