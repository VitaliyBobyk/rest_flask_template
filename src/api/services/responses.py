import json
from flask import current_app
from flask_restful import Resource, Api


class ResponseHandler(object):

    def _response(self, status, mimetype, response=None):
        return current_app.response_class(
            response=json.dumps(response),
            status=status,
            mimetype=mimetype
        )

    def success(self, status=200, mimetype='application/json', response=None):
        resp = {'success': True}
        if response:
            resp.update(response)
        return self._response(status, mimetype, resp)

    def error(self, status=400, mimetype='application/json', response=None):
        resp = {'success': False}
        if response:
            resp['errors'] = [response]
        return self._response(status, mimetype, resp)


class BaseApiClass(Resource, ResponseHandler):

    def get(self, *args, **kwargs):
        return self.error()

    def post(self, *args, **kwargs):
        return self.error()

    def put(self, *args, **kwargs):
        return self.error()

    def delete(self, *args, **kwargs):
        return self.error()
