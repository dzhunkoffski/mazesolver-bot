from aiogram import types
from loader import dp
from aiogram.types import InputFile
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command('example1'))
async def command_example1(msg: types.Message):
    await dp.bot.send_photo(chat_id=msg.from_user.id,
                            photo=InputFile(path_or_bytesio='media/examples/example1.jpg'))
    await msg.answer('Start point: 25 25; End point: 225 160')


@dp.message_handler(Command('example2'))
async def command_example2(msg: types.Message):
    await dp.bot.send_photo(chat_id=msg.from_user.id,
                            photo=InputFile(path_or_bytesio='media/examples/example2.jpg'))
    await msg.answer('Start point: 10 20; End point: 225 162')


@dp.message_handler(Command('example3'))
async def command_example3(msg: types.Message):
    await dp.bot.send_photo(chat_id=msg.from_user.id,
                            photo=InputFile(path_or_bytesio='media/examples/example3.jpg'))
    await msg.answer('Start point: 40 50; End point: 200 200')
