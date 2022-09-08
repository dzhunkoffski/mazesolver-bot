from aiogram.types import ContentType, Message
from loader import dp


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(msg: Message):
    await msg.reply(msg.photo[-1].file_id)

@dp.message_handler(text='/photo')
async def send_photo(msg: Message):
    photo_file_id = ''
    await dp.bot.send_photo(chat_id=msg.from_user.id, photo=photo_file_id)