import logging
import time

from PIL import Image
from aiogram import types

from config import WORKS_DIR
from database.schemas.processfile import ProcessFile


def resize_image(input_image_path, output_image_path, size):
    """
    Функция берёт изначальное изображение и отдаёт его ресайз копию.
    :param input_image_path:
    :param output_image_path:
    :param size:
    :return:
    """
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    logging.info(f'The original image size is {width} wide x {height} high')

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    logging.info(f'The resized image size is {width} wide x {height} high')

    resized_image.save(output_image_path)
    logging.debug(output_image_path)
    return output_image_path


async def prepare_to_do(message: types.Message) -> bool:
    """
    Функция скачивает и подготавливает изображение для обработки в Deep Nude.
    :param message:
    :return:
    """
    work_dir = WORKS_DIR
    user_id = message.from_user.id
    input_image = str(user_id) + str(time.time()) + '.jpg'
    path_to_save = work_dir + input_image

    try:
        # Download photo to server to $path_to_save
        await message.photo[-1].download(path_to_save)

        # Resize image for prepare to Deep Nude
        resize_image(input_image_path=path_to_save,
                     output_image_path=path_to_save,
                     size=(512, 512))

        # Add ProcessFile record
        await ProcessFile.create(user_id=int(user_id), input_image=input_image)

        return True
    except Exception as e:
        logging.info(f'ERROR Prepare - Exception: {e}')
        return False
