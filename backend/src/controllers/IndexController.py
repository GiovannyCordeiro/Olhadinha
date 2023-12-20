from flask import jsonify, request

class IndexController:
    def index():
        return jsonify({
        "status": "OK",
        "data": "Welcome to OLHADINHA API"
        })