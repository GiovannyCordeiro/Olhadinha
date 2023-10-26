from flask import request, abort

class IndexController:
    def index():
        origin = request.headers.get("Origin") 
        # if origin != "http://localhost:3050":
        #     abort(403)
        # if origin != "http://localhost:3000":
        #     abort(403)
        return {
        'status': 'OK',
        'data': "Welcome to OLHADINHA API",
        'origin': origin
        }