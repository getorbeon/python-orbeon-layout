import base64
from io import BytesIO
from PIL import Image
from ..utils import (    
    get_size,
    write_draw_rectangle
)


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
    write_draw_rectangle(image, coordinate)
    # logo_insert(image, coordinate, logo_base64)


def logo_insert(image, coordinate, logo_base64):
    width_ = coordinate['width'] - 5
    logo_image = get_logo_image(logo_base64, width_)
    box = get_center_middle_image_box(logo_image, coordinate)
    image.paste(logo_image, box)


def get_logo_image(logo_base64, width):
    logo_base64_bytes = base64.b64decode(logo_base64)
    logo_image = Image.open(BytesIO(logo_base64_bytes))
    if logo_image.mode != 'RGBA':
        logo_image = logo_image.convert('RGBA')
    logo_width, logo_height = logo_image.size
    logo_ratio = logo_width / logo_height
    logo_width_new = width * get_size()
    logo_height_new = round(logo_width_new / logo_ratio)
    new_size = (logo_width_new, logo_height_new)
    logo_image.resize(new_size, Image.LANCZOS)
    return logo_image


def get_center_middle_image_box(image, coordinate):

    # coordinate
    width = coordinate['width']
    height = coordinate['height']
    top = coordinate['top']
    left = coordinate['left']
    offset_left = coordinate['offset_left']
    offset_top = coordinate['offset_top']

    # height / width
    image_width, image_height = image.size
    image_width = image_width / get_size()
    image_height = image_height / get_size()
    
    # center / middle
    image_margin_center = (width - image_width) / 2
    image_margin_middle = (height - image_height) / 2

    # box
    box_left = round(image_margin_center + offset_left + left) * get_size()
    box_top = round(image_margin_middle + offset_top + top) * get_size()
    box = (box_left, box_top)

    return box
