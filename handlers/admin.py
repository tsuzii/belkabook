from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keybords import kb_admin, kb_client, admin_kb
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
import sqlite3 as sq


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    document = State()


# @dp.message_handler(commands="Добавить", state=None)
async def cm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузи фото', reply_markup=kb_admin)


# Выход из состояний
# @dp.message_handler(state='*', commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK", reply_markup=kb_client)


# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Введи название книги', reply_markup=kb_admin)


# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Добавь файл книги', reply_markup=kb_admin)


# @dp.message_handler(content_types=['document'], state=FSMAdmin.file)
async def load_document(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['document'] = message.document.file_id

    await sqlite_db.sql_add_command(state)
    await message.answer('Есть еще что добавить?', reply_markup=admin_kb.button_case_admin)
    await state.finish()

    # async with state.proxy() as data:
    #     await message.reply(str(data))


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(
        cm_start, commands=['Добавить'], state=None)
    dp.register_message_handler(cancel_handler, state='*', commands='Отмена')

    dp.register_message_handler(cancel_handler, Text(
        equals='Отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=[
                                'photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_document, content_types=[
                                'document'], state=FSMAdmin.document)
