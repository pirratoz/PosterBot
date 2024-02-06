from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from posterbot.utils.answers import TextTemplate
from posterbot.states import TemplateStates


async def fsm_set_title_start(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer(TextTemplate.AWAIT_TITLE_TEMPLATE)
    await state.set_state(TemplateStates.set_title)
    await callback.message.delete()
