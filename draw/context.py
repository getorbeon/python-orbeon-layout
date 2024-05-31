def get_context_clean(context_raw):
    cliente_nome, cliente_contato = get_cliente(context_raw)
    responsavel_nome, responsavel_contato = get_responsavel(context_raw)
    header = {
        'order_id':             context_raw['order_id'],
        'order_detail_url':     context_raw['qrcode_url'],
        'pid':                  context_raw['pid'],
        'layout':               context_raw['layout_id'],
        'layout_title':         get_title(context_raw['title']),
        'due_date':             get_data_retirada(context_raw['data_retirada']),
        'start_date':           get_data_inicio(),
        'customer_name':        cliente_nome,
        'customer_contact':     cliente_contato,
        'responsible_name':     responsavel_nome,
        'responsible_contact':  responsavel_contato,
        'products':             [],      
    }
    left = {
        'financial': context_raw['financeiro'].upper().strip(),
        'shipping': get_endereco(context_raw['entrega']),
        'obs': None,
    }
    right = {
        'body_image': context_raw['body_image'],
    }
    context = {
        'order': {},
        'header': header,
        'left': left,
        'right': right,
    }
    return context


def get_data_inicio():
    now = timezone.localtime(timezone.now())
    now_str = now.strftime('%d/%m/%y %H:%M')
    start_date = 'INÍCIO: {}'.format(now_str)
    return start_date


def get_data_retirada(data_inicio):
    if data_inicio:
        pass
    else:
        data_inicio = 'NÃO INFORMADA'
    data_inicio = 'ENTREGA: {}'.format(data_inicio)
    return data_inicio


def get_title(layout_title):
    layout_title = truncatechars(layout_title, 35).upper()
    return layout_title


def get_cliente(context_raw):
    cliente_nome = get_cliente_nome(context_raw['cliente_nome'])
    cliente_contato = get_cliente_contato(context_raw['cliente_contato'])
    return cliente_nome, cliente_contato


def get_cliente_nome(cliente_nome):
    customer_name = 'CLIENTE: {}'.format(cliente_nome).upper()
    customer_name = truncatechars(customer_name, 44)
    customer_name = customer_name.strip()
    return customer_name


def get_cliente_contato(cliente_contato):
    customer_contact = 'CONTATO: {}'.format(cliente_contato)
    customer_contact = truncatechars(customer_contact, 44)
    customer_contact = customer_contact.strip()
    return customer_contact


def get_responsavel(context_raw):

    responsavel_nome = context_raw['responsavel_nome']
    responsavel_contato = context_raw['responsavel_contato']

    responsible_name = 'RESPONSÁVEL: {}'.format(pretty_username(responsavel_nome)).upper()
    responsible_name = truncatechars(responsible_name, 44)
    responsible_name = responsible_name.strip()
    
    responsible_contact = 'CONTATO: {}'.format(responsavel_contato).upper()
    responsible_contact = truncatechars(responsible_contact, 44)
    responsible_contact = responsible_contact.strip()

    return responsible_name, responsible_contact


def get_endereco(entrega):

    shipping = {

        'method': {
            'title': 'MÉTODO:',
            'text': entrega['metodo'],
        },

        'public_place': {
            'title': 'LOGRADOURO:',
            'text': entrega['logradouro'],
        },

        'number': {
            'title': 'NÚMERO:',
            'text': entrega['numero'],
        },

        'complement': {
            'title': 'COMPLEMENTO:',
            'text': entrega['complemento'],
        },

        'neighborhood': {
            'title': 'BAIRRO:',
            'text': entrega['bairro'],
        },
        
        'city_uf': {
            'title': 'CIDADE/UF:',
            'text': entrega['cidade'] + '/' + entrega['uf'],
        },

        'cep': {
            'title': 'CEP:',
            'text': entrega['cep'],
        },

        'reference_point': {
            'title': 'PONTO DE REFERÊNCIA:',
            'text': entrega['ponto_de_referencia'],
        },

        'notes': {
            'title': 'OBSERVAÇÕES:',
            'text': entrega['observacoes'],
        },

    }

    return shipping


def truncatechars(value):
    return value


def pretty_username(value):
    return value