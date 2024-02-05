from aiogram.utils.magic_filter import MagicFilter
from aiogram import F

from posterbot.utils.commands import TemplateCallbackData
from posterbot.states import TemplateStates


class TemplateFilter:
    
    def SET_TITLE_TEMPLATE_FSM() -> list[MagicFilter]:
        return [
            (F.data == TemplateCallbackData.SET_TITLE)
        ]

    def SET_TITLE_TEMPLATE() -> list[MagicFilter]:
        return [
            TemplateStates.set_title
        ]
