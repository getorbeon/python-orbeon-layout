from ..import utils


def shipping(image, width, context):
    wrapper(image, width)
    title(context, image, width)
    body(image, width, context)


def wrapper(image, width):
    coordinate = {
        'width': width,
        'height': 82,
        'offset_left': 0,
        'offset_top': 41 + 2 + 20,
        'left': 0,
        'top': 2,
    }
    style = {
        'fill': '#fff',
        'outline': '#000',
        'stroke': 1,
    }
    utils.write_draw_rectangle_style(image, coordinate, style)


def title(context, image, width):
    coordinate = {
        'width': width,
        'height': 10,
        'offset_left': 0,
        'offset_top': 41 + 2 + 20,
        'left': 0,
        'top': 2,
    }
    style = {
        'fill': '#fff',
        'outline': '#000',
        'stroke': 1,
    }
    title_text = 'ENTREGA'
    utils.write_draw_rectangle_style(image, coordinate, style)
    title_font = 'MYRIADPRO-BOLD.OTF'
    title_font_fill = '#000'
    title_font_size = 15
    utils.write_text_center(image, coordinate, title_text, title_font, title_font_fill, title_font_size)


def body(image, width, context):
    coordinate = {
        'width': width,
        'height': 50 + 22,
        'offset_left': 0,
        'offset_top': 41 + 2 + 20 + 2 + 10,
        'left': 0,
        'top': 0,
    }
    style = {
        'fill': '#fff',
        'outline': 'blue',
        'stroke': 1,
    }
    utils.write_draw_rectangle_style(image, coordinate, style)
    body_method(image, width, context, coordinate)
    body_public_place(image, width, context, coordinate)
    body_number(image, width, context, coordinate)
    body_complement(image, width, context, coordinate)
    body_city_uf(image, width, context, coordinate)
    body_cep(image, width, context, coordinate)
    body_reference_point(image, width, context, coordinate)
    body_notes(image, width, context, coordinate)


def body_method(image, width, context, coordinate):
    # rectangle
    coordinate['height'] = 6
    utils.write_draw_rectangle_style(image, coordinate, {'fill': '#fff', 'outline': '#000', 'stroke': 1,})
    # title
    title_font = 'MYRIADPRO-BOLD.OTF'
    title_font_fill = '#000'
    title_font_size = 10
    text = context['shipping']['method']['title'].upper().strip()
    coordinate['top'] = coordinate['top'] + 2 
    coordinate['left'] = coordinate['left'] + 2 
    utils.write_text_left_top(image, coordinate, text, title_font, title_font_fill, title_font_size)
    # text
    text = context['shipping']['method']['text'].upper().strip()
    title_font = 'MYRIADPRO-REGULAR.OTF'
    coordinate['offset_left'] = coordinate['offset_left'] + 15
    utils.write_text_left_top(image, coordinate, text, title_font, title_font_fill, title_font_size)
    # reset
    coordinate['top'] = coordinate['top'] - 2
    coordinate['left'] = coordinate['left'] - 2
    coordinate['offset_top'] = coordinate['offset_top'] + 6
    coordinate['offset_left'] = coordinate['offset_left'] - 15


def body_public_place(image, width, context, coordinate):
    # rectangle
    coordinate['height'] = 15
    utils.write_draw_rectangle_style(image, coordinate, {'fill': '#fff', 'outline': '#000', 'stroke': 1,})
    # title
    coordinate['top'] = coordinate['top'] + 2
    coordinate['left'] = coordinate['left'] + 2
    method_title = context['shipping']['public_place']['title']
    title_font = 'MYRIADPRO-BOLD.OTF'
    title_font_fill = '#000'
    title_font_size = 10
    text = method_title.upper().strip()
    utils.write_text_left_top(image, coordinate, text, title_font, title_font_fill, title_font_size)
    # text
    text = context['shipping']['public_place']['text'].upper().strip()
    title_font = 'MYRIADPRO-REGULAR.OTF'
    coordinate['offset_top'] = coordinate['offset_top'] + 5
    utils.write_text_left_top(image, coordinate, text, title_font, title_font_fill, title_font_size)
    # reset
    coordinate['top'] = coordinate['top'] - 2
    coordinate['left'] = coordinate['left'] - 2
    coordinate['offset_top'] = coordinate['offset_top'] + coordinate['height'] - 5


def body_number(image, width, context, coordinate):
    # rectangle
    coordinate['height'] = 6
    utils.write_draw_rectangle_style(image, coordinate, {'fill': '#fff', 'outline': '#000', 'stroke': 1,})
    # title
    coordinate['top'] = coordinate['top'] + 2
    coordinate['left'] = coordinate['left'] + 2
    title_font = 'MYRIADPRO-BOLD.OTF'
    title_font_fill = '#000'
    title_font_size = 10
    text = context['shipping']['number']['title'].upper().strip()
    utils.write_text_left_top(image, coordinate, text, title_font, title_font_fill, title_font_size)
    # text
    text = context['shipping']['number']['text'].upper().strip()
    title_font = 'MYRIADPRO-REGULAR.OTF'
    coordinate['offset_left'] = coordinate['offset_left'] + 15
    utils.write_text_left_top(image, coordinate, text, title_font, title_font_fill, title_font_size)
    # reset
    coordinate['top'] = coordinate['top'] - 2
    coordinate['left'] = coordinate['left'] - 2
    coordinate['offset_left'] = coordinate['offset_left'] - 15
    coordinate['offset_top'] = coordinate['offset_top'] + 6


def body_complement(image, width, context, coordinate):
    # rectangle
    coordinate['height'] = 6
    utils.write_draw_rectangle_style(image, coordinate, {'fill': '#fff', 'outline': '#000', 'stroke': 1,})
    # title
    coordinate['top'] = coordinate['top'] + 2
    coordinate['left'] = coordinate['left'] + 2
    title_font = 'MYRIADPRO-BOLD.OTF'
    title_font_fill = '#000'
    title_font_size = 10
    text = context['shipping']['complement']['title'].upper().strip()
    utils.write_text_left_top(image, coordinate, text, title_font, title_font_fill, title_font_size)
    # text
    text = context['shipping']['complement']['text'].upper().strip()
    title_font = 'MYRIADPRO-REGULAR.OTF'
    coordinate['offset_left'] = coordinate['offset_left'] + 25
    utils.write_text_left_top(image, coordinate, text, title_font, title_font_fill, title_font_size)
    # reset
    coordinate['top'] = coordinate['top'] - 2
    coordinate['left'] = coordinate['left'] - 2
    coordinate['offset_left'] = coordinate['offset_left'] - 25
    coordinate['offset_top'] = coordinate['offset_top'] + 6


def body_city_uf(image, width, context, coordinate):
    # rectangle
    coordinate['height'] = 6
    utils.write_draw_rectangle_style(image, coordinate, {'fill': '#fff', 'outline': '#000', 'stroke': 1,})
    # title
    coordinate['top'] = coordinate['top'] + 2
    coordinate['left'] = coordinate['left'] + 2
    title_font = 'MYRIADPRO-BOLD.OTF'
    title_font_fill = '#000'
    title_font_size = 10
    text = context['shipping']['city_uf']['title'].upper().strip()
    utils.write_text_left_top(image, coordinate, text, title_font, title_font_fill, title_font_size)
    # text
    text = context['shipping']['city_uf']['text'].upper().strip()
    title_font = 'MYRIADPRO-REGULAR.OTF'
    coordinate['offset_left'] = coordinate['offset_left'] + 18
    utils.write_text_left_top(image, coordinate, text, title_font, title_font_fill, title_font_size)
    # reset
    coordinate['top'] = coordinate['top'] - 2
    coordinate['left'] = coordinate['left'] - 2
    coordinate['offset_left'] = coordinate['offset_left'] - 18
    coordinate['offset_top'] = coordinate['offset_top'] + 6


def body_cep(image, width, context, coordinate):
    # rectangle
    coordinate['height'] = 6
    utils.write_draw_rectangle_style(image, coordinate, {'fill': '#fff', 'outline': '#000', 'stroke': 1,})
    # title
    coordinate['top'] = coordinate['top'] + 2
    coordinate['left'] = coordinate['left'] + 2
    title_font = 'MYRIADPRO-BOLD.OTF'
    title_font_fill = '#000'
    title_font_size = 10
    text = context['shipping']['cep']['title'].upper().strip()
    utils.write_text_left_top(image, coordinate, text, title_font, title_font_fill, title_font_size)
    # text
    text = context['shipping']['cep']['text'].upper().strip()
    title_font = 'MYRIADPRO-REGULAR.OTF'
    coordinate['offset_left'] = coordinate['offset_left'] + 7
    utils.write_text_left_top(image, coordinate, text, title_font, title_font_fill, title_font_size)
    # reset
    coordinate['top'] = coordinate['top'] - 2
    coordinate['left'] = coordinate['left'] - 2
    coordinate['offset_left'] = coordinate['offset_left'] - 7
    coordinate['offset_top'] = coordinate['offset_top'] + 6


def body_reference_point(image, width, context, coordinate):
    # rectangle
    coordinate['height'] = 15
    style = {'fill': '#fff', 'outline': '#000', 'stroke': 1,}
    utils.write_draw_rectangle_style(image, coordinate, style)
    # title
    coordinate['top'] = coordinate['top'] + 2
    coordinate['left'] = coordinate['left'] + 2
    title_font = 'MYRIADPRO-BOLD.OTF'
    title_font_fill = '#000'
    title_font_size = 10
    text = context['shipping']['reference_point']['title'].upper().strip()
    utils.write_text_left_top(image, coordinate, text, title_font, title_font_fill, title_font_size)
    # text
    text = context['shipping']['reference_point']['text'].upper().strip()
    title_font = 'MYRIADPRO-REGULAR.OTF'
    coordinate['offset_top'] = coordinate['offset_top'] + 5
    utils.write_text_left_top(image, coordinate, text, title_font, title_font_fill, title_font_size)


def body_notes(image, width, context, coordinate):
    # rectangle
    coordinate['top'] = coordinate['top'] - 2
    coordinate['left'] = coordinate['left'] - 2
    coordinate['top'] = coordinate['top'] + 10
    coordinate['height'] = 12
    style = {'fill': '#fff', 'outline': '#000', 'stroke': 1,}
    utils.write_draw_rectangle_style(image, coordinate, style)
    # title
    coordinate['top'] = coordinate['top'] + 2
    coordinate['left'] = coordinate['left'] + 2
    title_font = 'MYRIADPRO-BOLD.OTF'
    title_font_fill = '#000'
    title_font_size = 10
    text = context['shipping']['notes']['title'].upper().strip()
    utils.write_text_left_top(image, coordinate, text, title_font, title_font_fill, title_font_size)
    # text
    coordinate['top'] = coordinate['top'] + 5
    text = context['shipping']['notes']['text']
    if not text: text = 'SEM OBSERVAÇÕES!'
    text = text.upper().strip()
    title_font = 'MYRIADPRO-REGULAR.OTF'
    utils.write_text_left_top(image, coordinate, text, title_font, title_font_fill, title_font_size)
