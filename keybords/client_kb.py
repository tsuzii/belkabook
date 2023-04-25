from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Поиск книги по названию')
b2 = KeyboardButton('/Добавить')
b3 = KeyboardButton('/Отмена')
b4 = KeyboardButton('Библиотека')
b5 = KeyboardButton('Назад')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_back = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b4).add(b2)
kb_back.add(b5)
kb_admin.add(b3)
