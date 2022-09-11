from aiogram import types
from loader import dp


@dp.message_handler(text='/start')
async def command_start(msg: types.Message):
    await msg.answer(f'Hello {msg.from_user.full_name}! \n'
                     f'Your ID {msg.from_user.id}')
