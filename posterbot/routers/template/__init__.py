__all__ = [
    "router_template",
]

from aiogram import Router

from posterbot.routers.template.fsm_fill_template_start import fsm_fill_template_start
from posterbot.routers.template.fsm_fill_template_end import fsm_fill_template_end
from posterbot.routers.template.fsm_set_title_start import fsm_set_title_start
from posterbot.routers.template.create_template import create_template
from posterbot.routers.template.remove_any_media import remove_any_media
from posterbot.routers.template.clear_template import clear_template
from posterbot.routers.template.show_template import show_template
from posterbot.routers.template.fill_template import fill_template
from posterbot.routers.template.remove_media import remove_media
from posterbot.routers.template.set_title import set_title

from posterbot.utils.filters import TemplateFilter


router_template = Router(name="template")


router_template.callback_query.register(
    fsm_set_title_start,
    *TemplateFilter.FSM_SET_TITLE_START()
)

router_template.message.register(
    set_title,
    *TemplateFilter.SET_TITLE_TEMPLATE()
)

router_template.callback_query.register(
    clear_template,
    *TemplateFilter.CLEAR_TEMPLATE()
)

router_template.callback_query.register(
    fsm_fill_template_start,
    *TemplateFilter.FSM_FILL_TEMPLATE_START()
)

router_template.callback_query.register(
    fsm_fill_template_end,
    *TemplateFilter.FSM_FILL_TEMPLATE_END()
)

router_template.message.register(
    fill_template,
    *TemplateFilter.FILL_TEMPLATE()
)

router_template.callback_query.register(
    remove_media,
    *TemplateFilter.REMOVE_MEDIA()
)

router_template.callback_query.register(
    show_template,
    *TemplateFilter.SHOW_TEMPLATE()
)

router_template.callback_query.register(
    remove_any_media,
    *TemplateFilter.REMOVE_MEDIA_LIST()
)
