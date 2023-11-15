import requests
import re

from bs4 import BeautifulSoup
from services.SavingDataService import SavingDataService
from helpers.Plataforms import indexPlatformsDB
from helpers.checkWitheSpaceStoreName import checkWitheSpaceStoreName

class MeuDimDimService:
    @staticmethod
    def extract(store:str) -> str:
        selectStore = checkWitheSpaceStoreName(store)
        url = f"https://www.meudimdim.com.br/loja/{selectStore.lower()}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
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