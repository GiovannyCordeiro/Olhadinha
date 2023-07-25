from flask import Blueprint
from controllers.TestController import TestController
from controllers.PlatformController import PlatformController

from services.dataSearchIntermediaryService import dataSearchIntermediaryService

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(dataSearchIntermediaryService.getAllPlatforms)
blueprint.route('/platform/<store>', methods=['GET'])(PlatformController.searchPlatforms)