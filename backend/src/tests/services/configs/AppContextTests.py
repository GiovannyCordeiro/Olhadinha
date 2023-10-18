from app import app
from functools import wraps

def app_context(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with app.get_app().app_context():
            return func(*args, **kwargs)
    return wrapper