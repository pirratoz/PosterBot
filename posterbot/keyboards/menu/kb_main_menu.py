from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from posterbot.utils.answers import MenuButtonText
from posterbot.utils.commands import MenuCallbackData


def kb_main_menu() -> InlineKeyboardMarkup:
    btn_moderator = InlineKeyboardButton(
        text=MenuButtonText.MODERATOR_MENU,
        callback_data=MenuCallbackData.MODERATOR_MENU
    )
    btn_template = InlineKeyboardButton(
        text=MenuButtonText.TEMPLATE_MENU,
        callback_data=MenuCallbackData.TEMPLATE_MENU
    )
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [btn_moderator],
            [btn_template],
        ]
    )
