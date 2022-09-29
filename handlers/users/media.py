# pylint: disable=missing-module-docstring

from aiogram.types import ContentType, Message
from loader import dp

@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(msg: Message):
    """Test function"""
    await msg.reply(msg.photo[-1].file_id)

@dp.message_handler(text='/photo')
async def send_photo(msg: Message):
    """Test function"""
    photo_file_id = ''
    await dp.bot.send_photo(chat_id=msg.from_user.id, photo=photo_file_id)