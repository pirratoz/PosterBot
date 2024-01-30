from aiogram.types import CallbackQuery
from aiogram import Bot

from source.services import (
    ServiceApiSession,
    ModerRequestBuilder,
)
from source.utils import (
    RegexpTemplate,
    AnswerText,
)


async def accept_moder_status(
    callback: CallbackQuery,
    bot: Bot,
    api: ServiceApiSession
) -> None:

    user_id_requesting_moderator: int = int(callback.data.split("_")[-1])
    fullname: str = RegexpTemplate.request_moder_fullname(callback.message.text)
    username: str = RegexpTemplate.requet_moder_username(callback.message.text)

    text = AnswerText.owner_accept_request_get_moderator
    
    response_request = await api.send(
        ModerRequestBuilder().create_moder(
            user_id_requesting_moderator,
            fullname,
            username
        )
    )

    if response_request.status == 201:
        text_for_owner = text
        await bot.send_message(user_id_requesting_moderator, text, parse_mode="html")
    elif response_request.status == 409:
        text_for_owner = AnswerText.moder_already_created
    else:
        text_for_owner = AnswerText.something_went_wrong

    await callback.message.answer(text_for_owner, parse_mode="html")
    await callback.message.delete()
