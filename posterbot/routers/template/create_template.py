from aiogram.types import CallbackQuery

from posterbot.services import TemplateRequestBuilder
from posterbot.services import ServiceApiSession
from posterbot.storages import (
    TemplateStorage,
    TemplateAction,
)
from posterbot.utils.answers import (
    TextTemplate,
    TextAnswer,
)


async def update_template(
    storage: TemplateAction,
    api: ServiceApiSession
) -> bool:
    
    response_data = await api.send(
        TemplateRequestBuilder().update_template(
            template_id=storage.template["id"],
            template=storage.template
        )
    )

    return response_data.status == 200


async def create_new_template(
    storage: TemplateAction,
    api: ServiceApiSession
) -> bool:
    
    response_data = await api.send(
        TemplateRequestBuilder().create_template(storage.template)
    )
    
    return response_data.status == 201


async def create_template(
    callback: CallbackQuery,
    storage_tmp: TemplateStorage,
    api: ServiceApiSession
) -> None:

    user_id = callback.message.chat.id
    storage = TemplateAction(storage_tmp, user_id)

    if not storage.template["text"] and not storage.template["media"]:
        await callback.message.answer(TextTemplate.TEMPLATE_CANNOT_BE_EMPTY)
        return None
    
    if not storage.template["title"]:
        await callback.message.answer(TextTemplate.TEMPLATE_TITLE_CANNOT_BE_EMPTY)
        return None
    
    is_new_template = storage.template["id"] is None

    text = TextAnswer.OOPS
    if is_new_template and await create_new_template(storage, api):
        text = TextTemplate.TEMPLATE_CREATED
        storage_tmp.clear(user_id)
    elif await update_template(storage, api):
        text = TextTemplate.TEMPLATE_UPDATED

    await callback.message.answer(text)
    await callback.answer()
