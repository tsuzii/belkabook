import telebot
import time
import logging

from aiogram import Bot, Dispatcher, executor, types

TOKEN = '5967772925:AAGsn7o7XiPNr4lzjU3ErAxSlrqS5zaFN7Q'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f"Приветствую тебя, {user_full_name}! Напиши название нужной тебе книги.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
