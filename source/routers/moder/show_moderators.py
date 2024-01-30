from aiogram.types import CallbackQuery

from source.configs import BotConfig
from source.services import (
    ModerRequestBuilder,
    ServiceApiSession,
)
from source.services.db import ModerManyResponse
from source.utils import (
    AnswerText,
)


async def show_moderators(
    callback: CallbackQuery,
    config: BotConfig,
    api: ServiceApiSession
) -> None:
    
    if callback.from_user.id not in config.OWNERS:
        return

    response_request = await api.send(
        ModerRequestBuilder().get_moders()
    )

    text = AnswerText.something_went_wrong
    if response_request.status == 200:
        moders = ModerManyResponse.model_validate(
            await response_request.json()
        ).moders
        moder_elements = [
            AnswerText.moder_list_element.format(**moder.model_dump())
            for moder in moders
        ]
        text = AnswerText.moder_list_title + "\n".join(moder_elements)
    
    await callback.message.answer(text=text, parse_mode="html")
    await callback.message.delete()
