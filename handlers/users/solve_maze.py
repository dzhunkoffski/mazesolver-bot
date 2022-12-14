# pylint: disable=missing-module-docstring
# pylint: disable=E1101

import shutil
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, InputFile
from aiogram.dispatcher.filters import Command
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from loader import dp
from states import Solve
from media import process_image
import graph

@dp.message_handler(Command('solve'))
async def solve(msg: types.Message):
    """Init solving pipeline"""
    await msg.answer('Send me picture of your maze')
    await Solve.waitImageState.set()


@dp.message_handler(state=Solve.waitImageState, content_types=[ContentType.PHOTO, ContentType.TEXT])
async def handle_maze_image(msg: types.Message, state: FSMContext):
    """Download image and resize it"""
    if not msg.photo:
        await msg.answer('This is not image, please send me image of the maze!!!')
    else:
        print('Image sent')
        await msg.answer('Downloading image...')
        await state.update_data(waitImageState=msg.photo)
        orig_image_name = f'media/{msg.photo[-1].file_id}/maze.jpg'
        await msg.photo[-1].download(orig_image_name)
        await msg.answer('Start image processing...')
        _, figure_path = process_image.prepare_image(orig_image_name, is_resize=True)
        await dp.bot.send_photo(chat_id=msg.from_user.id,
            photo=InputFile(path_or_bytesio=figure_path))
        await msg.answer('Choose start point in pixels, maze will be solved from')
        await Solve.waitStartPointState.set()


@dp.message_handler(state=Solve.waitStartPointState)
async def handle_startpoint(msg: types.Message, state: FSMContext):
    """Setting startpoint and validating it"""
    pos_x, pos_y = map(int, msg.text.split())
    data = await state.get_data()
    file_id = data.get('waitImageState')[-1]['file_id']
    figure_path = process_image.pick_start((pos_x, pos_y), 'media/' + file_id + '/maze.png')
    if figure_path == '':
        await msg.answer('You can not choose wall as a start_point, try again!!!')
    else:
        await dp.bot.send_photo(chat_id=msg.from_user.id,
            photo=InputFile(path_or_bytesio=figure_path))
        await state.update_data(waitStartPointState=(pos_x, pos_y))
        await msg.answer('Now choose end point in pixels')
        await Solve.waitEndPointState.set()


@dp.message_handler(state=Solve.waitEndPointState)
async def handle_endpoints(msg: types.Message, state: FSMContext):
    """Setting endpoint and validating it"""
    pos_x, pos_y = map(int, msg.text.split())

    data = await state.get_data()
    file_id = data.get('waitImageState')[-1]['file_id']
    flag = process_image.pick_end((pos_x, pos_y), 'media/' + file_id + '/maze.png')
    if flag == '':
        await msg.answer('You can not choose wall as a start_point, try again!!!')
    else:
        await state.update_data(waitEndPointState=(pos_x, pos_y))

        data = await state.get_data()
        img = cv2.imread('media/' + file_id + '/maze.png')
        start_point = data.get('waitStartPointState')
        end_point = data.get('waitEndPointState')
        cv2.circle(img, start_point, 3, (0, 255, 0), -1)
        cv2.circle(img, end_point, 3, (255, 0, 0), -1)
        plt.imshow(img)
        plt.savefig('media/' + file_id + '/maze_fig.png')
        await dp.bot.send_photo(chat_id=msg.from_user.id,
            photo=InputFile(path_or_bytesio='media/' + file_id + '/maze_fig.png'))

        await msg.answer('Start solving maze...')
        image = Image.open('media/' + file_id + '/maze.png')
        pixels = image.load()
        path = graph.solve_maze(image,
                                [start_point[0], start_point[1]],
                                [end_point[0], end_point[1]])
        await msg.answer('Found the shortest path!')
        for dots in path:
            pixels[dots[0], dots[1]] = (0, 0, 255)
        image.save('media/' + file_id + '/maze.png')

        img = cv2.imread('media/' + file_id + '/maze.png')
        cv2.circle(img, start_point, 3, (0, 255, 0), -1)
        cv2.circle(img, end_point, 3, (255, 0, 0), -1)
        plt.imshow(img)
        plt.savefig('media/' + file_id + '/maze_fig.png')
        await dp.bot.send_photo(chat_id=msg.from_user.id,
            photo=InputFile(path_or_bytesio='media/' + file_id + '/maze_fig.png'))

        shutil.rmtree(f'media/{file_id}')
        await state.finish()
