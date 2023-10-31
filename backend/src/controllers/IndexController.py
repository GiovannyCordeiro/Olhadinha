from flask import request, abort
import os

class IndexController:
    def index():
        origin = request.headers.get("Origin") 
        if os.environ['ENVIRONMENT_VARIABLE'] == "PROD":
            if origin != "http://localhost:3000":
                abort(403)

        return {
        'status': 'OK',
        'data': "Welcome to OLHADINHA API",
        'origin': origin
        }