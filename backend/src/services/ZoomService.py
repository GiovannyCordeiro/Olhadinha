import requests
import re

from bs4 import BeautifulSoup
from services.SavingDataService import SavingDataService
from helpers.Plataforms import indexPlatformsDB
from helpers.URLsScrapping import ULRsScrapping

class ZoomService:
    def extract(store: str) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        }
        url = ULRsScrapping.logic["zoom"](store)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        specificElement = soup.find('span',class_="Button_Label__TwuPX")
        if specificElement is None:
            return 'SNF'
        cashbackPercentage = re.split("%", specificElement.text[7:11])[0]
        SavingDataService.save(store.lower(), indexPlatformsDB['zoom'], cashbackPercentage)
        return cashbackPercentage