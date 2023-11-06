import requests
from bs4 import BeautifulSoup
from services.SavingDataService import SavingDataService
from helpers.Plataforms import indexPlatformsDB
import re

class ZoomService:
    def extract(store: str):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
        }
        url = f"https://www.zoom.com.br/search?q={store.lower()}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        specificElement = soup.find('span',class_="Text_Text__h_AF6 Text_DesktopLabelS__qDtn4 Chip_Text__WMVdR")
        if specificElement is None:
            return 'SNF'
        cashbackPercentage = re.split("%", specificElement.text[0:4])[0]
        SavingDataService.save(store.lower(), indexPlatformsDB['zoom'], cashbackPercentage)
        return cashbackPercentage