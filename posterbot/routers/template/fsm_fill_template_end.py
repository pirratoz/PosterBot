from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from posterbot.keyboards.menu import kb_template_menu
from posterbot.utils.answers import TextTemplate


async def fsm_fill_template_end(
    callback: CallbackQuery,
    state: FSMContext
) -> None:
    await callback.message.answer(
        text=TextTemplate.TEMPLATE_FILL_MODE_DISABLED,
        reply_markup=kb_template_menu()
    )
    await state.set_state(None)
    await callback.answer()
