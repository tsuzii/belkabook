from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Поиск_книги_по_названию')
b2 = KeyboardButton('/Добавить')
b3 = KeyboardButton('/Отмена')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2)
kb_admin.add(b3)
