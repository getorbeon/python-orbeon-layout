import textwrap
import datetime


def get_context_clean(context_raw):
    context = {
        'pid':                  context_raw['pid'],
        'layout':               context_raw['layout_id'],
        'title':         get_title(context_raw['title']),
        'due_date':             get_data_retirada(context_raw['data_retirada']),
        'start_date':           get_data_inicio(),
        'customer_name':        get_cliente_nome(context_raw),
        'customer_contact':     get_cliente_contato(context_raw),
        'responsible_name':     get_responsavel_nome(context_raw),
        'responsible_contact':  get_responsavel_contato(context_raw),
        'body_image':           context_raw['body_image'],
        'financial':            context_raw['financeiro'].upper().strip(),
        'entrega':              context_raw['entrega']
    }
    return context


def get_data_inicio():
    now = datetime.datetime.now()
    now_str = now.strftime('%d/%m/%y %H:%M')
    start_date = 'INÍCIO: {}'.format(now_str)
    return start_date


def get_data_retirada(data_retirada):
    if data_retirada:
        pass
    else:
        data_retirada = 'NÃO INFORMADA'
    data_retirada = 'CONCLUSÂO: {}'.format(data_retirada)
    return data_retirada


def get_title(layout_title):
    layout_title = truncatechars(layout_title, 35).upper()
    return layout_title


def get_cliente_nome(context_raw):
    cliente_nome = context_raw['cliente_nome']
    customer_name = 'CLIENTE: {}'.format(cliente_nome).upper()
    customer_name = truncatechars(customer_name, 60)
    customer_name = customer_name.strip()
    return customer_name


def get_cliente_contato(context_raw):
    cliente_contato = context_raw['cliente_contato']
    customer_contact = 'CONTATO: {}'.format(cliente_contato)
    customer_contact = customer_contact
    customer_contact = customer_contact.strip()
    return customer_contact


def get_responsavel_nome(context_raw):
    responsavel_nome = context_raw['responsavel_nome']
    responsavel_nome = truncatechars(responsavel_nome, 44)
    responsavel_nome = responsavel_nome.strip()
    return responsavel_nome


def get_responsavel_contato(context_raw):
    responsavel_contato = context_raw['responsavel_contato']
    responsavel_contato = 'CONTATO: {}'.format(responsavel_contato).upper()
    responsavel_contato = responsavel_contato
    responsavel_contato = responsavel_contato.strip()
    return responsavel_contato


def truncatechars(string, width=10):
    return textwrap.shorten(string, width=width, placeholder="...")