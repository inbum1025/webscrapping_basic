import requests
from bs4 import BeautifulSoup

url = "http://google.com"
res = requests.get(url)

res.raise_for_status()    # 문제가 생기면 바로 error 를 내뱉고 프로그램을 끝냄. 4,5 line 하고 세트


print(res.status_code)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)

print(len(res.text))
