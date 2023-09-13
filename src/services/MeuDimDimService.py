import requests
from bs4 import BeautifulSoup
from services.SavingDataService import SavingDataService
from helpers.Plataforms import indexPlatformsDB
import re

class MeuDimDimService:
    @staticmethod
    def extract(store:str):
        url = f"https://www.meudimdim.com.br/loja/{store}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        textElement = soup.find_all("h4")[0].text
        extractCashBack = textElement[16:18]
        dataCashback = re.split("%", extractCashBack)[0]
        SavingDataService.save(store, indexPlatformsDB['meudimdim'], dataCashback)
        return float(dataCashback)