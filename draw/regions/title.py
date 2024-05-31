from ..utils import write_text_center, write_draw_rectangle_style


def title(image, context):
    coordinate = {
        'width': 237,
        'height': 10,
        'offset_left': 57,
        'offset_top': 31,
        'left': 2,
        'top': 0,
    }
    style = {
        'fill': '#f7ffd9',
        'outline': '#000',
        'stroke': 1,
    }
    write_draw_rectangle_style(image, coordinate, style)
    value_text = context['title']
    value_font = 'MYRIADPRO-BOLD.OTF'
    value_font_fill = '#000'
    value_font_size = 15
    write_text_center(image, coordinate, value_text, value_font, value_font_fill, value_font_size)