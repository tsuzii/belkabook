from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '5967772925:AAGsn7o7XiPNr4lzjU3ErAxSlrqS5zaFN7Q'

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
