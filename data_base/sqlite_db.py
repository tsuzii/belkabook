import sqlite3 as sq
from create_bot import dp, bot
from handlers import client


def sql_start():
    global base, cur
    base = sq.connect('books.bd')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute(
        'CREATE TABLE IF NOT EXISTS library(img TEXT, name TEXT PRIMARY KEY, author TEXT, documents BLOB NOT NULL)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO library VALUES (?, ?, ?, ?)',
                    tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM library').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nАвтор: {ret[2]}')
        await bot.send_document(message.from_user.id, ret[3])


async def find_book(message):
    for ret in cur.execute('SELECT * FROM library').fetchall():
        if ret[1] == message:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nАвтор: {ret[2]}')
            await bot.send_document(message.from_user.id, ret[3])
