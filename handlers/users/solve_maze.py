from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType

from loader import dp
from aiogram.dispatcher.filters import Command

from states import Solve

from PIL import Image, ImageEnhance


@dp.message_handler(Command('solve'))
async def solve(msg: types.Message):
    await msg.answer('Send me picture of your maze')
    await Solve.waitImageState.set()


@dp.message_handler(state=Solve.waitImageState, content_types=[ContentType.PHOTO, ContentType.TEXT])
async def handle_maze_image(msg: types.Message, state: FSMContext):
    if not msg.photo:
        await msg.answer('This is not image, please send me image of the maze!!!')
    else:
        print('Image sent')
        await msg.answer('Downloading image...')
        await state.update_data(waitImageState=msg.photo)
        await msg.photo[-1].download(f'media/{msg.photo[-1].file_id}.jpg')
        img = Image.open(f'media/{msg.photo[-1].file_id}.jpg')
        await msg.answer(f'Maze image has size {img.size[0]}x{img.size[1]},\n'
                         f'now choose start point in pixels, maze will be solved from')
        await Solve.waitStartPointState.set()


@dp.message_handler(state=Solve.waitStartPointState)
async def handle_startpoint(msg: types.Message, state: FSMContext):
    x, y = map(int, msg.text.split())
    await state.update_data(waitStartPointState=[x, y])
    await msg.answer(f'now choose end point in pixels')
    await Solve.waitEndPointState.set()


@dp.message_handler(state=Solve.waitEndPointState)
async def handle_endpoints(msg: types.Message, state: FSMContext):
    x, y = map(int, msg.text.split())
    await state.update_data(waitEndPointState=[x, y])
    data = await state.get_data()
    sp_x = data.get('waitStartPointState')[0]
    sp_y = data.get('waitStartPointState')[1]
    ep_x = data.get('waitEndPointState')[0]
    ep_y = data.get('waitEndPointState')[1]
    await msg.answer(f'You choose start from ({sp_x}, {sp_y}) and end at ({ep_x}, {ep_y})')
    await state.finish()
