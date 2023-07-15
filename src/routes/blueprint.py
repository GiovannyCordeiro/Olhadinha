from flask import Blueprint
from controllers.TestController import TestController
from controllers.PlatformController import PlatformController

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(TestController.index)
blueprint.route('/platform/<store>', methods=['GET'])(PlatformController.searchPlataforms)