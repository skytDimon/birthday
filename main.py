import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

url = "https://dimdimich1120080.wordpress.com/"
r = requests.get(url=url, headers=headers)

soup = BeautifulSoup(r.text, "lxml")

with open("index.html", "w", encoding="utf-8") as file:
    file.write(r.text)