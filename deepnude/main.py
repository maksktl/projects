import asyncio
import logging

from cv2 import imread, imwrite

from database import db_gino
from database.processfile import ProcessFile
from run import process

from config import WORKS_DIR

"""
main.py

 How to run:
 python3 main.py

"""


def do_fake(input_image, work_dir=WORKS_DIR):
    output_image = 'out' + input_image
    logging.info(f'\n Work dir - {work_dir} \n input_image - {input_image}\n {output_image}')

    # Read input image
    dress = imread(work_dir + input_image)

    # Process
    watermark = process(dress)

    # Write output imag
    imwrite(work_dir + output_image, watermark)
    logging.info(f'\n READY TO RETURN !!!!!!!!!!  {output_image} saved in {work_dir}')
    return output_image


async def main():
    await db_gino.on_startup()
    while True:
        process_file = await ProcessFile.query.where(ProcessFile.process_completed == False).gino.first()
        logging.debug(process_file)
        if process_file:
            logging.info(f'Processfile is {process_file=}')
            try:
                fake_image = do_fake(input_image=process_file.input_image)
            except Exception as e:
                logging.info(f'ERROR --- {e}')
                logging.info(f'ERROR --- {e=}')
            else:
                await process_file.update(output_image=fake_image, process_completed=True).apply()
        else:
            await asyncio.sleep(5)


if __name__ == '__main__':
    logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                        level=logging.DEBUG)

    try:
        asyncio.run(main())
        logging.getLogger('asyncio').setLevel(logging.DEBUG)
    except Exception as e:
        logging.info(e)

# 3. Обаботка ошибок и завершение работы
