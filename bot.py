# pylint: disable=missing-module-docstring

from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

async def on_startup(dispatch):
    """What will bot do on a startup"""
    await on_startup_notify(dispatch)
    await set_default_commands(dispatch)


    print('Bot executed')

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
