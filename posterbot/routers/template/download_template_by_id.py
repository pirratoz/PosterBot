from aiogram.types import CallbackQuery

from posterbot.keyboards.menu import kb_template_menu
from posterbot.services.db.request import TemplateRequestBuilder
from posterbot.services.db.response import TemplateResponse
from posterbot.utils.commands.callbacks import TemplateCallbackRegexp
from posterbot.utils.answers import (
    TextTemplate,
    TextAnswer,
)
from posterbot.storages import (
    TemplateStorage,
    TemplateAction,
)
from posterbot.services import ServiceApiSession


async def download_template_by_id(
    callback: CallbackQuery,
    storage_tmp: TemplateStorage,
    api: ServiceApiSession
) -> None:
    
    template_id = TemplateCallbackRegexp().get_template_info(callback.data).template_id
    
    response_data = await api.send(
        TemplateRequestBuilder().get_template(template_id)
    )

    if response_data.status != 200:
        await callback.message.answer(TextAnswer.OOPS)

    template = TemplateResponse.model_validate(
        await response_data.json()
    )

    storage = TemplateAction(storage_tmp, callback.message.chat.id)

    storage.template["id"] = template.id
    storage.set_title(template.title)
    storage.set_text(template.text)
    storage.set_entities(template.attachments.entities)
    storage.template["media"] = [template.model_dump() for template in template.attachments.media]
    storage.template["keyboard"] = template.attachments.keyboard

    await callback.message.delete()
    await callback.message.answer(
        text=TextTemplate.TEMPLATE_DOWNLOADED,
        reply_markup=kb_template_menu()
    )
