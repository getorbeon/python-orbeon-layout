from ..import utils


def obs(image, width, context):
    obs_title(image, width)
    obs_body(image, width, context)


def obs_title(image, width):
    coordinate = {
        'width': width,
        'height': 10,
        'offset_left': 0,
        'offset_top': 41 + 2 + 20 + 2 + 82,
        'left': 0,
        'top': 2,
    }
    utils.write_draw_rectangle(image, coordinate)
    title_text = 'OBSERVAÇÕES'
    title_font = 'MYRIADPRO-BOLD.OTF'
    title_font_fill = '#000'
    title_font_size = 15
    coordinate['offset_top'] = coordinate['offset_top'] + 1
    utils.write_text_center(image, coordinate, title_text, title_font, title_font_fill, title_font_size)


def obs_body(image, width, context):
    coordinate = {
        'width': width,
        'height': 50,
        'offset_left': 0,
        'offset_top': 41 + 2 + 20 + 2 + 82 + 10 + 2,
        'left': 0,
        'top': 0,
    }
    style = {
        'fill': '#fff',
        'outline': '#000',
        'stroke': 1,
    }
    utils.write_draw_rectangle_style(image, coordinate, style)
    title_text = context['obs'].upper()
    title_font = 'MYRIADPRO-BOLD.OTF'
    title_font_fill = 'red'
    title_font_size = 11
    coordinate['left'] = coordinate['left'] + 2
    coordinate['top'] = coordinate['top'] + 2
    utils.write_text_left_top(image, coordinate, title_text, title_font, title_font_fill, title_font_size)
