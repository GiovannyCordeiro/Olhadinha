import requests
import re

from bs4 import BeautifulSoup
from services.SavingDataService import SavingDataService
from helpers.Plataforms import indexPlatformsDB

class CuponomiaService:
    def extract(store:str):
        selectStore = store
        storeNameWithSpace = re.match("\w+\s\w+", store)
        if storeNameWithSpace != None:
            splitingStore = store.split(" ")
            selectStore = "-".join(splitingStore)
        url = f"https://www.cuponomia.com.br/desconto/{selectStore.lower()}"
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