from flask import Blueprint
from controllers.IndexController import IndexController
from controllers.SearchStoreController import SearchStoreController

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/api', methods=['GET'])(IndexController.index)
blueprint.route('/api/platform/<store>', methods=['GET'])(SearchStoreController.controller)