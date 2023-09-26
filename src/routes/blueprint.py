from flask import Blueprint
from controllers.IndexController import IndexController
# from controllers.PlatformController import PlatformController

from services.DataSearchIntermediaryService import DataSearchIntermediaryService

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/platform/<store>', methods=['GET'])(DataSearchIntermediaryService.consultCashbackData)
blueprint.route('/', methods=['GET'])(IndexController.index)