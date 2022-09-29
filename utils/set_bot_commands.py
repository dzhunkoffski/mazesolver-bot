#pylint: disable=missing-module-docstring
from aiogram import types

async def set_default_commands(dispatcher):
    """Telegram bot commands"""
    await dispatcher.bot.set_my_commands([
        types.BotCommand('start', 'Execute the bot'),
        types.BotCommand('help', 'Help'),
        types.BotCommand('solve', 'Solve maze'),
        types.BotCommand('example1', 'Test bot with example 1'),
        types.BotCommand('example2', 'Test bot with example 2'),
        types.BotCommand('example3', 'Test bot with example 3')
    ])
