import telebot
import logging
import time

from aiogram.utils import executor
from keybords import kb_client, kb_admin
from create_bot import dp
from handlers import client, admin, other
from data_base import sqlite_db


sqlite_db.sql_start()

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True)
