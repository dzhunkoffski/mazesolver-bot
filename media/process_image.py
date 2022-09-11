from PIL import Image, ImageEnhance
import os
import cv2
import matplotlib.pyplot as plt


def resize_image(image, base_width=100):
    ratio = base_width / float(image.size[0])
    height = int(float(image.size[1]) * float(ratio))
    image = image.resize((base_width, height), Image.ANTIALIAS)
    return image


def prepare_image(image_path, is_resize=False):
    image_name = image_path.split('.')[0]
    image = Image.open(image_path)
    if is_resize and (image.size[0] > 250 or image.size[1] > 250):
        image = resize_image(image, 250)
    pixels = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            if pixels[i, j] < (192, 192, 192):
                pixels[i, j] = (0, 0, 0)
            else:
                pixels[i, j] = (255, 255, 255)
    image.save(image_name + '.png')
    image = cv2.imread(image_name + '.png')
    plt.imshow(image)
    plt.savefig(image_name + '_fig' + '.png')

    return image_name + '.png', image_name + '_fig' + '.png'


def pick_start(point, image_path):
    image_name = image_path.split('.')[0]
    image = Image.open(image_path)
    pixels = image.load()
    if pixels[point[0], point[1]] == (0, 0, 0):
        return ''
    img = cv2.imread(image_path)
    cv2.circle(img, point, 3, (0, 255, 0), -1)
    plt.imshow(img)
    plt.savefig(image_name + '_fig.png')

    return image_name + '_fig.png'


def pick_end(point, image_path):
    image = Image.open(image_path)
    pixels = image.load()
    if pixels[point[0], point[1]] == (0, 0, 0):
        return ''
    return 'good'
