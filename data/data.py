from datetime import datetime


def get_data():
    data = {
        'pid': '150',
        'layout_id': '15/20',
        'financeiro': 'LIBERADO',
        'data_inicio': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'data_conclusao': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'cliente_nome': 'JOÃO PEDRO DA SILVA COSTA QUENTE DO SUL E DO NORTE DO AMAZONAS',
        'cliente_contato': "(31) 9-8888-7777",
        'responsavel_nome': 'PEDRO LUCAS DA SILVA COSTA QUENTE DO SUL E DO NORTE DO PARÁ',
        'responsavel_contato': "(31) 9-8844-6644",
        'shipping': get_shipping(),
        'body_image_base64': get_body_image_base64(),
        'logo_image_base64': get_logo_image_base64(),
    }
    return data


def get_shipping():
    method = 'RETIRADA NA LOJA'
    public_place = 'Rua de Ouro'
    number = '456'
    complement = 'GALPAO A'
    neighborhood = 'Ouro Azul'
    city = 'Rio Preto'
    state_code = 'MG'
    postal_code = '30190110'
    location_reference = 'Prox. Club do Cruzeiro'
    note = 'Sucesso tem técnica'
    shipping = {
        'method': method,
        'public_place': public_place,
        'number': number,
        'complement': complement,
        'neighborhood': neighborhood,
        'city': city,
        'state_code': state_code,
        'postal_code': postal_code,
        'location_reference': location_reference,
        'notes': note,
    }
    return shipping


def get_body_image_base64():
    return ''


def get_logo_image_base64():
    return ''
