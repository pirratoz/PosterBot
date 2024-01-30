from aiogram.types import CallbackQuery

from source.services import (
    ModerRequestBuilder,
    ServiceApiSession,
)
from source.utils import AnswerText


async def demote_moderator_status(
    callback: CallbackQuery,
    api: ServiceApiSession
) -> None:

    moder_id: int = int(callback.data.split("_")[-1])

    response_request = await api.send(
        ModerRequestBuilder().delete_moder(moder_id)
    )

    text = AnswerText.something_went_wrong
    if response_request.status == 200:
        text = AnswerText.moder_demoted
    elif response_request.status == 404:
        text = AnswerText.moder_not_found

    await callback.message.answer(text)
    await callback.message.delete()
