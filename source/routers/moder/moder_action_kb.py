from aiogram.types import CallbackQuery

from source.utils import AnswerText
from source.keyboards import get_kb_moder_menu_action


async def moder_action_kb_menu(
    callback: CallbackQuery
) -> None:
    await callback.message.answer(
        AnswerText.moder_menu,
        reply_markup=get_kb_moder_menu_action()
    )
    await callback.message.delete()
