from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_load = KeyboardButton('Добавить')
button_delete = KeyboardButton('Назад')

button_case_admin = ReplyKeyboardMarkup(
    resize_keyboard=True).add(button_load).add(button_delete)
