from io import BytesIO
from .context import get_context_clean
from .utils import add_margin
from .regions.a4 import a4 as a4i
from .regions.data_inicio_conclusao import data_inicio, data_conclusao
from .regions.cliente_responsavel import cliente, responsavel
from .regions.title import title
from .regions.pid_layout import pid, layout
from .regions.financial import financial
from .regions.logo import logo
from .regions.body import body
from .regions.shopping import shipping_title, shipping_body
from .convert import encode_file_to_base64, get_image_name


def draw(context_raw):
    context = get_context_clean(context_raw)
    a4 = a4i()
    pid(a4, context)
    layout(a4, context)
    financial(a4, context)
    logo(a4, context)
    data_inicio(a4, context)
    data_conclusao(a4, context)
    cliente(a4, context)
    responsavel(a4, context)    
    shipping_title(a4, context)
    shipping_body(a4, context)
    title(a4, context)
    body(a4, context)
    a4 = add_margin(a4)
    result = get_final_result(a4)
    return result


def get_final_result(image):
    result = {
        'success': False,
        'filename': None,
        'error': None,
    }
    try:
        byte_io = BytesIO()
        image.save(byte_io, 'PNG')
        filename = get_image_name()
        file_io_values = byte_io.getvalue()
        filename = filename + '.png'
        file_data = encode_file_to_base64(file_io_values)
        result['filename'] = filename
        result['file_data'] = file_data
        result['success'] = True
    except Exception as e:
        result['error'] = str(e)
    return result
