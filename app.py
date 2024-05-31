from flask import Flask, request
from flask_restful import Resource, Api

from draw.main import draw
from draw.data import get_context_example_data


app = Flask(__name__)

api = Api(app)


class Main(Resource):

    def get(self):
        context = get_context_example_data('data_1.json')
        draw(context, True)
        return context

    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
        data = {
            'success': 'loading...'
        }
        return data, 201


api.add_resource(Main, '/')


if __name__ == '__main__':
    app.run(debug=True)