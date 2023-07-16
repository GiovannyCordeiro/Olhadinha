import requests
from bs4 import BeautifulSoup

class ZoomService:
    def extract(store):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
        }
        url = f"https://www.zoom.com.br/landing-page/cashback-zoom-{store}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        specifElement = soup.find_all('strong')[1].text
        cashbackPercentage = specifElement[1:4]
        return cashbackPercentage
