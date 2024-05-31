import io
import img2pdf

from .import utils


def convert(image, context):

    # context
    order = context['order']

    # Specify paper size (A4)
    a4inpt = (
        img2pdf.mm_to_pt(297),
        img2pdf.mm_to_pt(210)
    )
    layout_fun = img2pdf.get_layout_fun(a4inpt)

    # Image PNG to PDF A4
    byte_io = io.BytesIO()
    image.save(byte_io, 'PNG')
    layout_pdf_a4 = img2pdf.convert(
        byte_io.getvalue(),
        layout_fun=layout_fun
    )

    # Save in django
    file_name = utils.get_image_name()

    layout_content_file_pdf = ContentFile(
        layout_pdf_a4,
        file_name + '.pdf'
    )

    layout_content_file_img = ContentFile(
        byte_io.getvalue(),
        file_name + '.png'
    )

    # create layout in db
    Layout.objects.create(
        title=file_name,
        order=order,
        layout_pdf=layout_content_file_pdf,
        layout_img=layout_content_file_img,
    )
