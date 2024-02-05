from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from posterbot.utils.answers.button import (
    ModeratorButtonText,
    MenuButtonText,
)
from posterbot.utils.commands.callbacks import (
    ModeratorCallbackData,
    MenuCallbackData,
)


def kb_moderator_menu() -> InlineKeyboardMarkup:
    btn_show_moderators = InlineKeyboardButton(
        text=ModeratorButtonText.SHOW_MODERATORS,
        callback_data=ModeratorCallbackData.SHOW_MODERATORS
    )
    btn_show_moderators_for_demote = InlineKeyboardButton(
        text=ModeratorButtonText.SHOW_MODERATORS_FOR_DEMOTE,
        callback_data=ModeratorCallbackData.SHOW_MODERATORS_FOR_DEMOTE
    )
    btn_return_to_main_menu = InlineKeyboardButton(
        text=MenuButtonText.MAIN_MENU,
        callback_data=MenuCallbackData.MAIN_MENU
    )
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [btn_show_moderators],
            [btn_show_moderators_for_demote],
            [btn_return_to_main_menu]
        ]
    )
