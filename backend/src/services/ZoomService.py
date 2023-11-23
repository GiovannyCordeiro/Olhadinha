import requests
import re

from bs4 import BeautifulSoup
from services.SavingDataService import SavingDataService
from helpers.Plataforms import indexPlatformsDB
from helpers.URLsScrapping import ULRsScrapping

class ZoomService:
    def extract(store: str) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
        }
        url = ULRsScrapping.logic["zoom"](store)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        specificElement = soup.find('span',class_="Button_Label__5DJmK")
        if specificElement is None:
            return 'SNF'
        cashbackPercentage = re.split("%", specificElement.text[7:11])[0]
        SavingDataService.save(store.lower(), indexPlatformsDB['zoom'], cashbackPercentage)
        return cashbackPercentage