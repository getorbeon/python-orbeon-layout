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

from .convert import convert


def draw(context_raw):
    result = get_initial_result()
    context = get_context_clean(context_raw)
    a4 = a4i()
    pid(a4, context)
    layout(a4, context)
    financial(a4, 57, context)
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
    result = get_final_result(a4, result)
    return result


def get_initial_result():
    result = {
        'success': False,
        'filename': None,
        'files': {
            'img': None,
            'pdf': None,
        },
        'error': None,
    }
    return result


def get_final_result(a4, result):
    filename, img, pdf = convert(a4)
    result['filename'] = filename
    result['files']['img'] = img
    result['files']['pdf'] = pdf
    result['success'] = True
    return result