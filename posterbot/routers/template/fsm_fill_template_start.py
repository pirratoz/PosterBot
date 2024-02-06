from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from posterbot.utils.answers import TextTemplate
from posterbot.states import TemplateStates


async def fsm_fill_template_start(
    callback: CallbackQuery,
    state: FSMContext
) -> None:
    await callback.message.answer(TextTemplate.TEMPLATE_FILL_MODE_ENABLED)
    await state.set_state(TemplateStates.fill_tmp)
    await callback.message.delete()
