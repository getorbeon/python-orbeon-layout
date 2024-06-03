from decouple import config


def authenticate(json_data):
    result = False
    try:
        token_request = json_data.get('token', None)
        token_app = config('TOKEN', None)
        if token_app:
            if len(token_app) > 3:
                if token_request == token_app:
                    result = True
    except Exception as e:
        pass
    return result