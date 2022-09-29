# pylint: disable=missing-module-docstring

from aiogram import types
from loader import dp

@dp.message_handler(text='/help')
async def command_help(msg: types.Message):
    """Help command"""
    await msg.answer('Run /solve command in the bot')
