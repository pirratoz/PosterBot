from aiogram.types import CallbackQuery

from posterbot.keyboards.menu.kb_template_menu import kb_template_menu
from posterbot.utils.commands.callbacks import TemplateCallbackRegexp
from posterbot.services.db.request import PublicationRequestBuilder
from posterbot.services.db.response import PublicationManyResponse
from posterbot.services.db.request import TemplateRequestBuilder
from posterbot.utils.answers import TextTemplate
from posterbot.services import ServiceApiSession
from posterbot.utils.answers import TextAnswer
from posterbot.storages import TemplateStorage


async def check_template_in_publications(
    template_id: int,
    api: ServiceApiSession
) -> tuple[bool | None, int]:
    
    response = False
    count = 0

    response_data = await api.send(
        PublicationRequestBuilder().get_publication_active()
    )
    if response_data.status != 200:
        return (None, count)

    publications = PublicationManyResponse.model_validate(
        await response_data.json()
    )

    for publication in publications.publications:
        if publication.template_id == template_id:
            response = True
    return (response, count)


async def check_template_in_templates(
    template_id: int,
    api: ServiceApiSession
) -> bool | None:
    response_data = await api.send(
        TemplateRequestBuilder().get_template(template_id)
    )
    
    responses = {
        404: False,
        200: True 
    }
    
    return responses.get(response_data.status, None)


async def delete_template(
    template_id: int,
    api: ServiceApiSession
) -> bool:
    response_data = await api.send(
        TemplateRequestBuilder().delete_template(template_id)
    )
    return response_data.status == 200


async def confirm_delete_template(
    callback: CallbackQuery,
    api: ServiceApiSession,
    storage_tmp: TemplateStorage
) -> None:
    
    text = TextAnswer.OOPS
    
    template_id = TemplateCallbackRegexp().get_template_info(callback.data).template_id

    in_publication, count_publication = await check_template_in_publications(
        template_id,
        api
    )
    in_template = await check_template_in_publications(
        template_id,
        api
    )

    if in_template:
        text = TextTemplate.TEMPLATE_DELETED

    if in_publication:
        text = TextTemplate.TEMPLATE_DELETED_WITH_N_PUBLICATIONS(
            count_publication=count_publication
        )
    
    if in_template or in_publication:
        if not await delete_template(template_id, api):
            text = TextAnswer.OOPS
            storage_tmp.clear(callback.message.chat.id)

    await callback.message.delete()
    await callback.message.answer(
        text=text,
        markup=kb_template_menu()
    )
