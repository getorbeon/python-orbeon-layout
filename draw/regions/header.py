from ..import utils


def header(a4, context):
    context = context['header']
    logo(a4, context)
    pid(a4, context)
    layout(a4, context)
    qr_code(a4, context)
    start_date(a4, context)
    due_date(a4, context)
    customer(a4, context)
    responsible(a4, context)
    products_head(a4, context)
    products_body(a4, context)


def logo(image, context):
    coordinate = {
        'width': 57,
        'height': 20,
        'offset_left': 0,
        'offset_top': 0,
        'left': 0,
        'top': 0,
    }
    utils.write_draw_rectangle(image, coordinate)
    logo_insert(image, coordinate)


def logo_insert(image, coordinate):
    width_ = coordinate['width'] - 20
    logo_image = utils.get_logo_image(width_)
    box = utils.get_center_middle_image_box(logo_image, coordinate)
    image.paste(logo_image, box, logo_image)


def pid(image, context):
    
    # TITLE
    coordinate = {
        'width': 27,
        'height': 10,
        'offset_left': 0,
        'offset_top': 22,
        'left': 0,
        'top': 0,
    }
    utils.write_draw_rectangle(image, coordinate)
    pid_title_text = 'PEDIDO'
    pid_title_font = 'MYRIADPRO-BOLD.OTF'
    pid_title_font_fill = '#000'
    pid_title_font_size = 18
    utils.write_text_center(image, coordinate, pid_title_text, pid_title_font, pid_title_font_fill, pid_title_font_size)

    # VALUE
    coordinate = {
        'width': 27,
        'height': 10,
        'offset_left': 0,
        'offset_top': 22 + 10 - 1,
        'left': 0,
        'top': 0,
    }
    utils.write_draw_rectangle(image, coordinate)
    pid_value_text = context['pid']
    pid_value_font = 'MYRIADPRO-BOLD.OTF'
    pid_value_font_fill = '#000'
    pid_value_font_size = 18
    utils.write_text_center(image, coordinate, pid_value_text, pid_value_font, pid_value_font_fill, pid_value_font_size)


def layout(image, context):
    # TITLE
    coordinate = {
        'width': 27,
        'height': 10,
        'offset_left': 3 + 27,
        'offset_top': 22,
        'left': 0,
        'top': 0,
    }
    utils.write_draw_rectangle(image, coordinate)
    layout_title_text = 'LAYOUT'
    layout_title_font = 'MYRIADPRO-BOLD.OTF'
    layout_title_font_fill = '#000'
    layout_title_font_size = 18
    utils.write_text_center(image, coordinate, layout_title_text, layout_title_font, layout_title_font_fill, layout_title_font_size)
    # VALUE
    coordinate = {
        'width': 27,
        'height': 10,
        'offset_left': 3 + 27,
        'offset_top': 22 + 10 - 1,
        'left': 0,
        'top': 0,
    }
    utils.write_draw_rectangle(image, coordinate)
    layout_value_text = context['layout']
    layout_value_font = 'MYRIADPRO-BOLD.OTF'
    layout_value_font_fill = '#000'
    layout_value_font_size = 18
    utils.write_text_center(image, coordinate, layout_value_text, layout_value_font, layout_value_font_fill, layout_value_font_size)


def qr_code(image, context):
    coordinate = {
        'width': 41,
        'height': 41,
        'offset_left': 59,
        'offset_top': 0,
        'left': 0,
        'top': 0,
    }
    utils.write_draw_rectangle(image, coordinate)
    qr_code_insert(image, context, coordinate)


def qr_code_insert(image, context, coordinate):
    qrcode_data = context['order_detail_url']
    width_ = coordinate['width'] + coordinate['offset_left'] + 10
    qrcode_image = utils.get_qrcode_image(qrcode_data, width_)
    box = utils.get_center_middle_image_box(qrcode_image, coordinate)
    image.paste(qrcode_image, box)


def start_date(image, context):
    coordinate = {
        'width': 45,
        'height': 10,
        'offset_left': 57 + 2 + 41 + 2,
        'offset_top': 0,
        'left': 0,
        'top': 0,
    }
    style = {
        'fill': '#CEE2C0',
        'outline': '#000',
        'stroke': 1,
    }
    utils.write_draw_rectangle_style(image, coordinate, style)
    due_date_value_text = context['start_date']
    due_date_value_font = 'MYRIADPRO-BOLD.OTF'
    due_date_value_font_fill = '#000'
    due_date_value_font_size = 11
    utils.write_text_center(image, coordinate, due_date_value_text, due_date_value_font, due_date_value_font_fill, due_date_value_font_size)


def due_date(image, context):
    coordinate = {
        'width': 46,
        'height': 10,
        'offset_left': 57 + 2 + 41 + 2 + 45 + 1,
        'offset_top': 0,
        'left': 0,
        'top': 0,
    }
    style = {
        'fill': '#ff8b8b',
        'outline': '#000',
        'stroke': 1,
    }
    utils.write_draw_rectangle_style(image, coordinate, style)
    due_date_value_text = context['due_date']
    due_date_value_font = 'MYRIADPRO-BOLD.OTF'
    due_date_value_font_fill = '#000'
    due_date_value_font_size = 11
    utils.write_text_center(image, coordinate, due_date_value_text, due_date_value_font, due_date_value_font_fill, due_date_value_font_size)


def customer(image, context):
    coordinate = {
        'width': 92,
        'height': 14,
        'offset_left': 57 + 2 + 41 + 2,
        'offset_top': 3 + 8,
        'left': 0,
        'top': 0,
    }
    style = {
        'fill': '#fff',
        'outline': '#000',
        'stroke': 1,
    }
    utils.write_draw_rectangle_style(image, coordinate, style)
    value_text = context['customer_name'] + '\n' + context['customer_contact']
    value_font = 'MYRIADPRO-REGULAR.OTF'
    value_font_fill = '#000'
    value_font_size = 13
    coordinate['offset_left'] = coordinate['offset_left'] + 2
    utils.write_text_left(image, coordinate, value_text, value_font, value_font_fill, value_font_size)


def responsible(image, context):
    coordinate = {
        'width': 92,
        'height': 15,
        'offset_left': 57 + 2 + 41 + 2,
        'offset_top': 3 + 10 + 1 + 8 + 8 - 4,
        'left': 0,
        'top': 0,
    }
    style = {
        'fill': '#fff',
        'outline': '#000',
        'stroke': 1,
    }
    utils.write_draw_rectangle_style(image, coordinate, style)
    value_text = context['responsible_name'] + '\n' + context['responsible_contact']
    value_font = 'MYRIADPRO-REGULAR.OTF'
    value_font_fill = '#000'
    value_font_size = 13
    coordinate['offset_left'] = coordinate['offset_left'] + 2
    utils.write_text_left(image, coordinate, value_text, value_font, value_font_fill, value_font_size)


def products_head(image, context):
    coordinate = {
        'width': 100,
        'height': 10,
        'offset_left': 57 + 2 + 41 + 2 + 92 + 2,
        'offset_top': 0,
        'left': 0,
        'top': 0,
    }
    style = {
        'fill': '#f7ffd9',
        'outline': '#000',
        'stroke': 1,
    }
    utils.write_draw_rectangle_style(image, coordinate, style)
    value_text = context['layout_title']
    value_font = 'MYRIADPRO-BOLD.OTF'
    value_font_fill = '#000'
    value_font_size = 15
    utils.write_text_center(image, coordinate, value_text, value_font, value_font_fill, value_font_size)


def products_body(image, context):
    coordinate = {
        'width': 100,
        'height': 30,
        'offset_left': 57 + 2 + 41 + 2 + 92 + 2,
        'offset_top': 10,
        'left': 0,
        'top': 1,
    }
    utils.write_draw_rectangle(image, coordinate)
    products_text = ''
    for product in context['products']:
        product_text = product
        products_text = products_text + '\n' + product_text
    value_text = products_text
    value_font = 'MYRIADPRO-REGULAR.OTF'
    value_font_fill = '#000'
    value_font_size = 9
    coordinate['offset_left'] = coordinate['offset_left'] + 2
    utils.write_text_left_top(image, coordinate, value_text, value_font, value_font_fill, value_font_size)