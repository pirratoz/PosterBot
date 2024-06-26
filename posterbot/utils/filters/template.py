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
            TemplateStates.fill_tmp
        ]

    def REMOVE_MEDIA() -> list[MagicFilter]:
        return [
            (F.data.startswith(TemplateCallbackData.REMOVE_MEDIA))
        ]

    def SHOW_TEMPLATE() -> list[MagicFilter]:
        return [
            (F.data == TemplateCallbackData.SHOW_TEMPLATE)
        ]

    def REMOVE_MEDIA_LIST() -> list[MagicFilter]:
        return [
            (F.data == TemplateCallbackData.REMOVE_MEDIA_LIST)
        ]

    def CREATE_TEMPLATE() -> list[MagicFilter]:
        return [
            (F.data == TemplateCallbackData.CREATE_TEMPLATE)
        ]
    
    def SELECT_TEMPLATE() -> list[MagicFilter]:
        return [
            (F.data == TemplateCallbackData.SELECT_TEMPLATE)
        ]

    def DOWNLOAD_TEMPLATE() -> list[MagicFilter]:
        return [
            (F.data.startswith(TemplateCallbackData.DOWNLOAD_TEMPLATE_BY_ID))
        ]

    def DELETE_TEMPLATE() -> list[MagicFilter]:
        return [
            (F.data == TemplateCallbackData.DELTE_TEMPLATE)
        ]
    
    def CONFIRM_DELETE_TEMPLATE() -> list[MagicFilter]:
        return [
            (F.data.startswith(TemplateCallbackData.CONFIRM_DELTE_TEMPLATE))
        ]
