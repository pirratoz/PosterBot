from aiogram.utils.magic_filter import MagicFilter
from aiogram import F

from posterbot.configs import BotConfig
from posterbot.utils.commands.text import MenuTextCommand
from posterbot.utils.commands.callbacks import (
    MenuMainCallbackData,
    MenuModeratorCallbackData,
)


class MenuFilter:
    
    def MAIN_MENU() -> list[MagicFilter]:
        return [
            (F.text.lower().in_(MenuTextCommand.SHOW_MAIN_MENU)) |
            (F.data == MenuMainCallbackData.SHOW_MENU)
        ]

    def MODERATOR_MENU() -> list[MagicFilter]:
        return [
            (F.data == MenuModeratorCallbackData.SHOW_MENU) &
            (F.from_user.id.in_(BotConfig().OWNERS))
        ]
