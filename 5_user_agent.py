import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"}
url = "http://google.com"
res = requests.get(url, headers=headers)
res.raise_for_status()    # 문제가 생기면 바로 error 를 내뱉고 프로그램을 끝냄. 4,5 line 하고 세트

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
