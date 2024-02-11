from aiogram.utils.magic_filter import MagicFilter
from aiogram import F

from posterbot.utils.commands.text import ChatTextCommand


class ChatFilter:
    
    def APPEND_OR_REMOVE_CHAT() -> list[MagicFilter]:
        return [
            (F.text.lower().in_(ChatTextCommand.APPEND_OR_REMOVE_CHAT))
        ]
