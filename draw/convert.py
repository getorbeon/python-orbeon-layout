import base64

from io import BytesIO
import img2pdf
import datetime


def convert(image):

    # Specify paper size (A4)
    a4inpt = (img2pdf.mm_to_pt(297), img2pdf.mm_to_pt(210))
    layout_fun = img2pdf.get_layout_fun(a4inpt)

    # Image PNG to PDF A4
    byte_io = BytesIO()
    image.save(byte_io, 'PNG')
    layout_pdf_a4 = img2pdf.convert(byte_io.getvalue(), layout_fun=layout_fun)

    # Save in django
    filename = get_image_name()

    # img
    img_data = byte_io.getvalue()
    img = {
        'filename': filename + '.png',
        'data': encode_file_to_base64(img_data),
    }

    # pdf
    pdf_data = layout_pdf_a4
    pdf = {
        'filename': filename + '.pdf',
        'data': encode_file_to_base64(pdf_data),
    }

    return filename, img, pdf


def encode_file_to_base64(file_data):
    file_base64_string = None
    if file_data:
        file_data_io = BytesIO(file_data)
        file_base64_string = base64.b64encode(file_data_io.getvalue()).decode()
    return file_base64_string


def get_image_name():
    now_format = '%Y_%m_%d_%H%M%S_%f'
    now = datetime.datetime.now()
    now_string = now.strftime(now_format)
    layout_file_name = '{}_{}'.format('layout', now_string)
    return layout_file_name