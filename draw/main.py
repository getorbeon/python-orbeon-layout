from .regions.a4 import a4 as a4i
from .regions.header import header
from .regions.left import left
from .regions.right import right
from .context import get_context_clean

from .utils import add_margin
from .convert_to_pdf_a4 import convert as convert_to_pdf_a4_convert


def draw(context_raw):

    context = get_context_clean(context_raw)

    a4 = a4i()

    # H: 41 (header) + 2 (space)
    # W: 297
    header(a4, context)

    # H: 20 (financial) + 2 (space) + 82 (shipping) + 2 (space) + 60 (obs) + 1 (space) 
    # W: 57 + 2
    left(a4, context)

    # 57 / 2 / 237 / 1
    right(a4, context)

    a4 = add_margin(a4)

    convert_to_pdf_a4_convert(a4, context)