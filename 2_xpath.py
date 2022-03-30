import bs4
import requests
from bs4 import BeautifulSoup
from soupsieve import select_one


url = 'https://www.naver.com'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    menu = soup.find("div", {"id": "NM_ONELINE_ROLLING"})

    print(menu.text)

else:
    print(response.status_code)
