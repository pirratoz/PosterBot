from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from posterbot.utils.answers.button import (
    MenuButtonText,
)
from posterbot.utils.commands.callbacks import (
    MenuCallbackData,
)


def kb_template_menu() -> InlineKeyboardMarkup:
    btn_return_to_main_menu = InlineKeyboardButton(
        text=MenuButtonText.MAIN_MENU,
        callback_data=MenuCallbackData.MAIN_MENU
    )
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [btn_return_to_main_menu]
        ]
    )
