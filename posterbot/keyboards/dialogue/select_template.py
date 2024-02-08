from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from posterbot.services.db.response import TemplateManyResponse
from posterbot.utils.commands import TemplateCallbackBuilder


def kb_select_template(templates: TemplateManyResponse) -> InlineKeyboardMarkup:
    STEP = 2
    btns = [
        InlineKeyboardButton(
            text=template.title,
            callback_data=TemplateCallbackBuilder().download_template(template.id)
        )
        for template in templates.templates
    ]
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                btns[i:i+STEP]
            ]
            for i in range(0, len(templates.templates), STEP)
        ]
    )
