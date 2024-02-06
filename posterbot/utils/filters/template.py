from aiogram.utils.magic_filter import MagicFilter
from aiogram import F

from posterbot.utils.commands import TemplateCallbackData
from posterbot.states import TemplateStates


class TemplateFilter:
    
    def FSM_SET_TITLE_START() -> list[MagicFilter]:
        return [
            (F.data == TemplateCallbackData.SET_TITLE)
        ]

    def SET_TITLE_TEMPLATE() -> list[MagicFilter]:
        return [
            TemplateStates.set_title
        ]
    
    def CLEAR_TEMPLATE() -> list[MagicFilter]:
        return [
            (F.data == TemplateCallbackData.CLEAR_TEMPLATE)
        ]

    def FSM_FILL_TEMPLATE_START() -> list[MagicFilter]:
        return [
            (F.data == TemplateCallbackData.FILL_TEMPLATE_START)
        ]

    def FSM_FILL_TEMPLATE_END() -> list[MagicFilter]:
        return [
            (F.data == TemplateCallbackData.FILL_TEMPLATE_END)
        ]

    def FILL_TEMPLATE() -> list[MagicFilter]:
        return [
            (F.video) |
            (F.photo) |
            (F.text) |
            (F.caption)
        ]

    def REMOVE_MEDIA() -> list[MagicFilter]:
        return [
            (F.data.startswith(TemplateCallbackData.REMOVE_MEDIA))
        ]

    def SHOW_TEMPLATE() -> list[MagicFilter]:
        return [
            (F.data == TemplateCallbackData.SHOW_TEMPLATE)
        ]
