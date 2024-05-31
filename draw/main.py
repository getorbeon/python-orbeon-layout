from pathlib import Path

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

from .convert_to_pdf_a4 import convert as convert_to_pdf_a4_convert


def draw(context_raw, debug=False):
    context = get_context_clean(context_raw)
    a4 = a4i()
    pid(a4, context)
    layout(a4, context)
    financial(a4, 57, context)
    logo(a4)
    data_inicio(a4, context)
    data_conclusao(a4, context)
    cliente(a4, context)
    responsavel(a4, context)
    shipping_title(a4, context)
    shipping_body(a4, context)
    title(a4, context)
    body(a4, context, debug)
    a4 = add_margin(a4)
    # convert_to_pdf_a4_convert(a4, context)
    if debug:
        path = Path(__file__).parent.parent.joinpath('examples').joinpath('ex.png')
        a4.save(path)
    else:
        print('Tá em producao, porra!')