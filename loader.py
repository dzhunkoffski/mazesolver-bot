# pylint: disable=missing-module-docstring

import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=os.environ['BOT_TOKEN'], parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
