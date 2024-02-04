from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from posterbot.utils.answers import MenuButtonText
from posterbot.utils.commands.callbacks import MenuModeratorCallbackData


def kb_main_menu() -> InlineKeyboardMarkup:
    btn_moderator = InlineKeyboardButton(
        text=MenuButtonText.MODERATOR_MENU,
        callback_data=MenuModeratorCallbackData.SHOW_MENU
    )
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [btn_moderator]
        ]
    )
