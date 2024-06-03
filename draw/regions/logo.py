import base64
from io import BytesIO

from PIL import Image

from ..import utils
from ..utils import get_size


def logo(image, context):
    logo_base64 = context['logo_base64']
    coordinate = {
        'width': 35,
        'height': 29,
        'offset_left': 59,
        'offset_top': 0,
        'left': 0,
        'top': 0,
    }
    utils.write_draw_rectangle(image, coordinate)
    logo_insert(image, coordinate, logo_base64)


def logo_insert(image, coordinate, logo_base64):
    width_ = coordinate['width'] - 5
    logo_image = get_logo_image(width_, logo_base64)
    box = utils.get_center_middle_image_box(logo_image, coordinate)
    image.paste(logo_image, box, logo_image)


def get_logo_image(width, logo_base64):
    width = width * get_size()
    logo_base64_bytes = base64.b64decode(logo_base64)
    logo_image = Image.open(BytesIO(logo_base64_bytes))
    logo_width, logo_height = logo_image.size
    logo_ratio = logo_width / logo_height
    logo_width_new = width
    logo_height_new = round(logo_width_new / logo_ratio)
    new_size = (logo_width_new, logo_height_new)
    logo_image = logo_image.resize(new_size, Image.ANTIALIAS)
    return logo_image