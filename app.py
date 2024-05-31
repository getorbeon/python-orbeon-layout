from flask import Flask
from flask_restful import Resource, Api

from draw.context import get_context_clean
from .ex import get_context_example_data


app = Flask(__name__)

api = Api(app)


class HelloWorld(Resource):
    def get(self):
        context_clean = get_context_clean(get_context_example_data())
        return context_clean


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)