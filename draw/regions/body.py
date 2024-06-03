from ..utils import (
    write_draw_rectangle,
    get_center_middle_image_box,
    get_body_image
)


def body(image, context):
    coordinate = {
        'width': 296,
        'height': 166,
        'offset_left': 0,
        'offset_top': 41,
        'left': 0,
        'top': 2,
    }
    write_draw_rectangle(image, coordinate)
    body_image_insert(image, coordinate, context)


def body_image_insert(image, coordinate, context):
    width_ = coordinate['width'] - 2
    height_ = coordinate['height'] - 2
    body_image = get_body_image(context, width_, height_)
    box = get_center_middle_image_box(body_image, coordinate)
    image.paste(body_image, box)