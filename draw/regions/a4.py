from PIL import Image

from ..import utils


def a4():

    size = utils.get_size()

    A4H = 210
    
    A4W = 297

    width = A4W * size

    height = A4H * size

    a4_image_fill = 'white'

    a4_image = Image.new('RGB', (width, height), a4_image_fill)

    return a4_image