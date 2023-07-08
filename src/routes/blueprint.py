from flask import Blueprint
from controllers.TestController import TestController

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(TestController.index)