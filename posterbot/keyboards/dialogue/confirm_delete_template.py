from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from posterbot.utils.answers import TemplateButtonText
from posterbot.utils.commands import TemplateCallbackBuilder


def kb_confirm_delete_template(template_id: int) -> InlineKeyboardMarkup:
    btn_confirm_delete = InlineKeyboardButton(
        text=TemplateButtonText.CONFIRM_DELETE_TEMPLATE,
        callback_data=TemplateCallbackBuilder.confirm_delete(template_id)
    )
    return InlineKeyboardMarkup(inline_keyboard=[
        [btn_confirm_delete]
    ])
