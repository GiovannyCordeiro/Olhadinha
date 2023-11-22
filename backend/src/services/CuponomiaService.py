import requests

from bs4 import BeautifulSoup
from services.SavingDataService import SavingDataService
from helpers.Plataforms import indexPlatformsDB
from helpers.URLsScrapping import ULRsScrapping


class CuponomiaService:
    def extract(store:str) -> str:
        url = ULRsScrapping.logic["cuponomia"](store)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        textElement = soup.find(class_="rewardsTag-cashback")
        if textElement is None:
            cashbackPercentage = "SNF"
        else:
            cashbackPercentage = textElement.text[8:9]
        SavingDataService.save(store.lower(), indexPlatformsDB['cuponomia'], cashbackPercentage)
        return cashbackPercentage