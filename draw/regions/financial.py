from ..utils import (
    write_draw_rectangle,
    write_text_center,
    write_draw_rectangle_style
)


def financial(image, width, context):
    financial_title(image, width)
    financial_body(image, width, context)


def financial_title(image, width):
    coordinate = {
        'width': width,
        'height': 10,
        'offset_left': 0,
        'offset_top': 21,
        'left': 0,
        'top': 0,
    }
    write_draw_rectangle(image, coordinate)
    pid_title_text = 'FINANCEIRO'
    pid_title_font = 'MYRIADPRO-BOLD.OTF'
    pid_title_font_fill = '#000'
    pid_title_font_size = 15
    write_text_center(image, coordinate, pid_title_text, pid_title_font, pid_title_font_fill, pid_title_font_size)


def financial_body(image, width, context):
    financeiro_status = context['financial'].upper()
    financeiro_fill = 'yellow'
    pid_title_font_fill = '#000'
    if financeiro_status == 'LIBERADO':
        financeiro_fill = 'green'
        pid_title_font_fill = '#fff'
    coordinate = {
        'width': width,
        'height': 10,
        'offset_left': 0,
        'offset_top': 31,
        'left': 0,
        'top': 0,
    }
    style = {
        'fill': financeiro_fill,
        'outline': '#000',
        'stroke': 1,
    }
    write_draw_rectangle_style(image, coordinate, style)
    pid_title_text = financeiro_status
    pid_title_font = 'MYRIADPRO-BOLD.OTF'
    pid_title_font_size = 15
    write_text_center(image, coordinate, pid_title_text, pid_title_font, pid_title_font_fill, pid_title_font_size)