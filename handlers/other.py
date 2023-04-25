from aiogram import types, Dispatcher
from create_bot import dp, bot
from keybords import kb_client


# @dp.message_handler()
async def empty(message: types.Message):
    await message.answer('Нет такой команды', reply_markup=kb_client)
    await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(empty)
