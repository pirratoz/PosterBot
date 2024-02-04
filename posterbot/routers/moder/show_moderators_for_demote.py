from aiogram.types import CallbackQuery

from posterbot.services.db.response import ModerManyResponse
from posterbot.keyboards.dialogue import kb_demote_moderator
from posterbot.utils.answers import (
    TextModerator,
    TextAnswer,
)
from posterbot.services import (
    ModerRequestBuilder,
    ServiceApiSession,
)


async def get_moders(api: ServiceApiSession) -> ModerManyResponse | None:
    request_data = await api.send(ModerRequestBuilder().get_moders())
    if request_data.status == 200:
        return ModerManyResponse.model_validate(
            await request_data.json()
        )
    return None


async def show_moderators_for_demote(
    callback: CallbackQuery,
    api: ServiceApiSession
) -> None:
    
    moders = await get_moders(api)

    if moders:
        await callback.message.answer(
            text=TextModerator.WHO_TO_DEMOTE,
            reply_markup=kb_demote_moderator(moders)
        )
    else:
        await callback.message.answer(TextAnswer.OOPS)
    
    await callback.message.delete()
