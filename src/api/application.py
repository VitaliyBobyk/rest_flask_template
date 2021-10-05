from flask import Flask, request
from flask_restful import Api

from services.responses import BaseApiClass

app = Flask(__name__)
api = Api(app)


class HelloWorld(BaseApiClass):
    def get(self, *args, **kwargs):
        return self.success(response={'msg': 'success'})
    def post(self, *args, **kwargs):
        return self.success(response={'msg': 'success'})



api.add_resource(HelloWorld, '/hello_world/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
