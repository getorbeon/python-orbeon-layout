from flask import Flask
from flask_restful import Resource, Api
from draw.main import draw_form

app = Flask(__name__)

api = Api(app)


class HelloWorld(Resource):
    def get(self):
        context = {
            'Success': True,
            'It is ok?': 'Tudo certo!',
        }
        draw_form(context)
        return {'success': True}


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)