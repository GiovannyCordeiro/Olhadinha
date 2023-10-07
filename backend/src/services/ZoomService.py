import requests
from bs4 import BeautifulSoup
from services.SavingDataService import SavingDataService
from helpers.Plataforms import indexPlatformsDB
import re

class ZoomService:
    def extract(store:str):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
        }
        url = f"https://www.zoom.com.br/landing-page/cashback-zoom-{store}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        specificElement = soup.find_all('strong')[1].text
        onlyPorcentage = re.split("%", specificElement)[0]
        cashbackPercentage = onlyPorcentage[1:4]
        if cashbackPercentage == "":
            cashbackPercentage = "SNF"
        SavingDataService.save(store, indexPlatformsDB['zoom'], cashbackPercentage)
        return cashbackPercentage
