from aiogram.types import CallbackQuery

from posterbot.keyboards.dialogue import kb_confirm_delete_template
from posterbot.services.db.request import PublicationRequestBuilder
from posterbot.services.db.response import PublicationManyResponse
from posterbot.utils.answers import TextTemplate
from posterbot.services import ServiceApiSession
from posterbot.utils.answers import TextAnswer
from posterbot.storages import (
    TemplateStorage,
    TemplateAction,
)


async def check_template_in_publications(
    template_id: int,
    api: ServiceApiSession
) -> bool | None:
    response_data = await api.send(
        PublicationRequestBuilder().get_publication_active()
    )
    if response_data.status != 200:
        return None
    
    publications = PublicationManyResponse.model_validate(
        await response_data.json()
    )

    for publication in publications.publications:
        if publication.template_id == template_id:
            return True
    return False


async def delete_template(
    callback: CallbackQuery,
    api: ServiceApiSession,
    storage_tmp: TemplateStorage
) -> None:
    
    user_id = callback.message.chat.id
    
    storage = TemplateAction(storage_tmp, user_id)
    
    markup = None
    text = TextTemplate.TEMPLATE_NOT_FOUND_IN_DATABASE
    if storage.template["id"]:
        template_used = await check_template_in_publications(
            storage.template["id"],
            api
        )
        if template_used == None:
            text = TextAnswer.OOPS
        elif template_used:
            text = TextTemplate.TEMPLATE_ALREADY_USED_IN_PUBLICATION
            markup = kb_confirm_delete_template(storage.template["id"])
        else:
            text = TextTemplate.CONFIRM_TEMPLATE_DELETE
            markup = kb_confirm_delete_template(storage.template["id"])

    await callback.message.answer(text, reply_markup=markup)
    await callback.message.delete()
