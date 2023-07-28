from flask import Blueprint
from controllers.TestController import TestController
from controllers.PlatformController import PlatformController

from services.DataSearchIntermediaryService import DataSearchIntermediaryService

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(DataSearchIntermediaryService.consultCashbackData)
blueprint.route('/platform/<store>', methods=['GET'])(PlatformController.searchPlatforms)