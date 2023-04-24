from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp
from aiogram import types, Dispatcher


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    file = State()


# @dp.message_handler(commands="Добавить", state=None)
async def cm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузи фото')


# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Введи название книги')


# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Добавь файл книги')


# @dp.message_handler(content_types=['document'], state=FSMAdmin.file)
async def load_file(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['document'] = message.document[0].file_id
    async with state.proxy() as data:
        await message.reply(str(data))

    await state.finish()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(
        cm_start, commands=['addadminbook'], state=None)
    dp.register_message_handler(load_photo, content_types=[
                                'photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_file, content_types=[
                                'document'], state=FSMAdmin.file)
