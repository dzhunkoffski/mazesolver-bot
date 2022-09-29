# pylint: disable=missing-module-docstring
# pylint: disable=W0703

import logging
from aiogram import Dispatcher
from data.config import admin_ids

async def on_startup_notify(dispathcer: Dispatcher):
    """Notifies bot's administrators"""
    for admin in admin_ids:
        try:
            await dispathcer.bot.send_message(admin, text='Bot executed')
        except Exception as err:
            await logging.exception(err)
