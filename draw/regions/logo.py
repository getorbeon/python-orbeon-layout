from ..import utils


def logo(image):
    coordinate = {
        'width': 35,
        'height': 29,
        'offset_left': 59,
        'offset_top': 0,
        'left': 0,
        'top': 0,
    }
    utils.write_draw_rectangle(image, coordinate)
    logo_insert(image, coordinate)


def logo_insert(image, coordinate):
    width_ = coordinate['width'] - 5
    logo_image = utils.get_logo_image(width_)
    box = utils.get_center_middle_image_box(logo_image, coordinate)
    image.paste(logo_image, box, logo_image)
