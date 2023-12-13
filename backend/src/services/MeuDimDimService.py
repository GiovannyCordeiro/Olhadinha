import requests
import re

from bs4 import BeautifulSoup
from services.SavingDataService import SavingDataService
from helpers.Plataforms import indexPlatformsDB
from helpers.URLsScrapping import ULRsScrapping

class MeuDimDimService:
    @staticmethod
    def extract(store:str) -> str:
        urlForSearch = store
        if urlForSearch == "madesa":
            urlForSearch = "loja-madesa"
        url = ULRsScrapping.logic['meudimdim'](urlForSearch)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        textElement = soup.find_all("h4")[0].text
        extractCashBack = textElement[16:19]
        dataCashback = re.split("%", extractCashBack)[0]
        if dataCashback == "":
            dataCashback = "SNF"
        SavingDataService.save(store.lower(), indexPlatformsDB['meudimdim'], dataCashback)
        return dataCashback