from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from posterbot.utils.answers.button import (
    MenuButtonText,
    TemplateButtonText,
)
from posterbot.utils.commands.callbacks import (
    TemplateCallbackData,
    MenuCallbackData,
)


def kb_template_menu() -> InlineKeyboardMarkup:
    btn_clear_tmp = InlineKeyboardButton(
        text=TemplateButtonText.CLEAR_TEMPLATE,
        callback_data=TemplateCallbackData.CLEAR_TEMPLATE
    )
    btn_set_title = InlineKeyboardButton(
        text=TemplateButtonText.SET_TITLE,
        callback_data=TemplateCallbackData.SET_TITLE
    )
    btn_fill_tmp = InlineKeyboardButton(
        text=TemplateButtonText.FILL_TEMPLATE,
        callback_data=TemplateCallbackData.FILL_TEMPLATE_START
    )
    btn_show_tmp = InlineKeyboardButton(
        text=TemplateButtonText.SHOW_TEMPLATE,
        callback_data=TemplateCallbackData.SHOW_TEMPLATE
    )
    btn_create_tmp = InlineKeyboardButton(
        text=TemplateButtonText.CREATE_TEMPLATE,
        callback_data=TemplateCallbackData.CREATE_TEMPLATE
    )
    btn_return_to_main_menu = InlineKeyboardButton(
        text=MenuButtonText.MAIN_MENU,
        callback_data=MenuCallbackData.MAIN_MENU
    )
    btn_remove_any_media = InlineKeyboardButton(
        text=TemplateButtonText.REMOVE_MEDIA,
        callback_data=TemplateCallbackData.REMOVE_MEDIA_LIST
    )
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [btn_clear_tmp],
            [btn_set_title],
            [btn_fill_tmp],
            [btn_remove_any_media],
            [btn_show_tmp, btn_create_tmp],
            [btn_return_to_main_menu]
        ]
    )
