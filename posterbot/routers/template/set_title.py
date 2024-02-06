from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from posterbot.keyboards.menu import kb_template_menu
from posterbot.utils.answers import TextTemplate
from posterbot.storages import (
    TemplateStorage,
    TemplateAction,
)


async def set_title(
    message: Message,
    state: FSMContext,
    storage_tmp: TemplateStorage
) -> None:

    if not message.text:
        await message.answer(
            TextTemplate.TITLE_TEMPLATE_NOT_BE_NONE
        )
        return None

    storage = TemplateAction(storage_tmp, message.from_user.id)
    storage.set_title(message.text)

    await state.set_state(None)

    await message.answer(
        TextTemplate.TITLE_SETTED.format(title=message.text),
        reply_markup=kb_template_menu()
    )
