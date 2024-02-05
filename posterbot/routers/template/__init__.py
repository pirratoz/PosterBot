__all__ = [
    "router_template",
]

from aiogram import Router

from posterbot.routers.template.set_title import (set_title_fsm, set_title)

from posterbot.utils.filters import TemplateFilter


router_template = Router(name="template")


router_template.callback_query.register(
    set_title_fsm,
    *TemplateFilter.SET_TITLE_TEMPLATE_FSM()
)

router_template.message.register(
    set_title,
    *TemplateFilter.SET_TITLE_TEMPLATE()
)
