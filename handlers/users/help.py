from loader import dp
from aiogram import types

@dp.message_handler(text='/help')
async def command_help(msg: types.Message):
    await msg.answer('Lol help')