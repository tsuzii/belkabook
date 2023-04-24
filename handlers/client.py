import logging
import time


from aiogram import types, Dispatcher
from create_bot import dp, bot
from keybords import kb_client
from aiogram.types import ReplyKeyboardRemove

logging.basicConfig(level=logging.INFO)


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f"Приветствую тебя, {user_full_name}!", reply_markup=kb_client)


# @dp.message_handler(commands=['Поиск книги по названию'])
async def find(message: types.Message):
    await bot.send_message(message.from_user.id, "сча попроуем найти", reply_markup=ReplyKeyboardRemove())


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(find, commands=['Поиск_книги_по_названию'])
