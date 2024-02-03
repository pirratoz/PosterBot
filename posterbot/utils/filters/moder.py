from aiogram.utils.magic_filter import MagicFilter
from aiogram.enums import ChatType
from aiogram import F

from posterbot.configs import BotConfig
from posterbot.utils.commands import (
    ModeratorCallbackData,
    ModeratorTextCommand,
)


class ModeratorFilter:
    
    def REQUEST_STATUS_MODERATOR() -> list[MagicFilter]:
        return [
            (F.text == ModeratorTextCommand.REQUEST_STATUS_MODERATOR) &
            (F.chat.type == ChatType.PRIVATE)
        ]

    def ACCEPT_STATUS_MODERATOR() -> list[MagicFilter]:
        return [
            (F.data.startswith(ModeratorCallbackData.ACCEPT_STATUS_MODERATOR)) &
            (F.chat.type == ChatType.PRIVATE)
        ]

    def REJECT_STATUS_MODERATOR() -> list[MagicFilter]:
        return [
            (F.data.startswith(ModeratorCallbackData.REJECT_STATUS_MODERATOR)) &
            (F.chat.type == ChatType.PRIVATE)
        ]

    def SHOW_MODERATORS() -> list[MagicFilter]:
        return [
            (F.data.startswith(ModeratorCallbackData.SHOW_MODERATORS)) &
            (F.from_user.id.in_(BotConfig().OWNERS)) &
            (F.chat.type == ChatType.PRIVATE)
        ]

    def SHOW_MODERATORS_FOR_DEMOTE() -> list[MagicFilter]:
        return [
            (F.data.startswith(ModeratorCallbackData.SHOW_MODERATORS_FOR_DEMOTE)) &
            (F.from_user.id.in_(BotConfig().OWNERS)) &
            (F.chat.type == ChatType.PRIVATE)
        ]

    def DEMOTE_STATUS_MODERATOR() -> list[MagicFilter]:
        return [
            (F.data.startswith(ModeratorCallbackData.DEMOTE_MODERATOR)) &
            (F.from_user.id.in_(BotConfig().OWNERS)) &
            (F.chat.type == ChatType.PRIVATE)
        ]
