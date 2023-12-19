from flask import jsonify

class IndexController:
    def index():
        return jsonify({
        'status': 'OK',
        'data': "Welcome to OLHADINHA API"
        })