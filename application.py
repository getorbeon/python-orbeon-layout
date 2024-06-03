from flask import Flask, request
from flask_restful import Resource, Api
from decouple import config
from draw.main import draw
from draw.auth import authenticate


app = Flask(__name__)

api = Api(app)


class Welcome(Resource):

    def get(self):
        return {'working': True}, 200


class LayoutGenerator(Resource):

    def post(self):
        status_code = 500
        response_data = {
            'success': False,
            'files': None,
            'error': None,
        }
        try:
            json_data = request.get_json()
            authenticated = authenticate(json_data)
            if authenticated:
                response_data = draw(json_data)
                status_code = 201
            else:
                status_code = 401
                response_data['error'] = 'Sem token ou token inválido.'
        except Exception as e:
            response_data['error'] = str(e)
        return response_data, status_code


api.add_resource(Welcome, '/')
api.add_resource(LayoutGenerator, '/layout-generator')


if __name__ == '__main__':
    app.run(debug=config('DEBUG', default=False, cast=bool))
    app.run()