import logging
import time


from aiogram import types, Dispatcher
from create_bot import dp, bot
from keybords import kb_client, kb_admin
from keybords import kb_back
from aiogram.types import ReplyKeyboardRemove

logging.basicConfig(level=logging.INFO)


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.delete()
    await message.answer(f"Приветствую тебя, {user_full_name}!", reply_markup=kb_client)


@dp.message_handler(lambda message: message.text.startswith("Назад"))
async def find(message: types.Message):
    await bot.send_message(message.from_user.id, 'OK', reply_markup=kb_client)


# @dp.message_handler(commands=['Поиск книги по названию'])
# async def find(message: types.Message):
#     await bot.send_message(message.from_user.id, "сча попроуем найти", reply_markup=ReplyKeyboardRemove())
@dp.message_handler(lambda message: message.text.startswith("Поиск книги по названию"))
async def find(message: types.Message):
    await message.reply("сча попроуем найти", reply_markup=kb_back)


@dp.message_handler(lambda message: message.text.startswith("Библиотека"))
async def find(message: types.Message):
    await message.reply("сча попроуем найти", reply_markup=kb_back)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    # dp.register_message_handler(find, commands=['Поиск книги по названию'])
