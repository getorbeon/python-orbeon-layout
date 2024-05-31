from ..import utils


def right(image, context):
    right_context = context['right']
    body(image, right_context)


def body(image, context):
    coordinate = {
        'width': 237,
        'height': 166,
        'offset_left': 57,
        'offset_top': 41,
        'left': 2,
        'top': 2,
    }
    utils.write_draw_rectangle(image, coordinate)
    body_image_insert(image, coordinate, context)


def body_image_insert(image, coordinate, context):
    width_ = coordinate['width'] - 2
    height_ = coordinate['height'] - 2
    body_image = utils.get_body_image(context, width_, height_, False)
    box = utils.get_center_middle_image_box(body_image, coordinate)
    image.paste(body_image, box)
