
from flask import request

from services.DataSearchIntermediaryService import DataSearchIntermediaryService
from helpers.security.CheckHeaderFront import CheckHeaderFront

class SearchStoreController:
    def controller(store: str):
        CheckHeaderFront(request.headers.get("Confirmation-From-Front")).validate()
        return DataSearchIntermediaryService.consultCashbackData(store)