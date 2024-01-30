from aiogram.types import CallbackQuery

from source.services.db import ModerManyResponse
from source.services import (
    ModerRequestBuilder,
    ServiceApiSession,
)
from source.utils import AnswerText
from source.keyboards import get_kb_demote_moder_menu


async def demote_moderator_list(
    callback: CallbackQuery,
    api: ServiceApiSession
) -> None:

    response_request = await api.send(
        ModerRequestBuilder().get_moders()
    )

    text = AnswerText.something_went_wrong
    keyboard = None
    if response_request.status == 200:
        moders = ModerManyResponse.model_validate(
            await response_request.json()
        ).moders
        keyboard = get_kb_demote_moder_menu(moders)
        text = AnswerText.demote_moder_title

    await callback.message.answer(text, reply_markup=keyboard)
    await callback.message.delete()
