from aiogram.types import CallbackQuery

from posterbot.keyboards.dialogue import kb_select_template
from posterbot.services.db.request import TemplateRequestBuilder
from posterbot.services.db.response import TemplateManyResponse
from posterbot.utils.answers import (
    TextTemplate,
    TextAnswer,
)
from posterbot.services import ServiceApiSession


async def select_template(
    callback: CallbackQuery,
    api: ServiceApiSession
) -> None:
    
    response_data = await api.send(
        TemplateRequestBuilder().get_templates()
    )

    if response_data.status != 200:
        await callback.message.answer(TextAnswer.OOPS)

    templates = TemplateManyResponse.model_validate(
        await response_data.json()
    )

    if templates.templates:
        await callback.message.answer(
            text=TextTemplate.SELECT_TEMPLATE,
            reply_markup=kb_select_template(templates)
        )
        await callback.message.delete()
    else:
        await callback.message.answer(
            text=TextTemplate.TEMPLATES_IS_EMPTY
        )
