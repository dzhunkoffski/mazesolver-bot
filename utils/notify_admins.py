import logging

from aiogram import Dispatcher

from data.config import admin_ids

async def on_startup_notify(dp: Dispatcher):
    for admin in admin_ids:
        try:
            await dp.bot.send_message(admin, text='Bot executed')
        except Exception as e:
            await logging.exception(e)