import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
respuesta = requests.get(url)

soup = BeautifulSoup(respuesta.text, features="html.parser")

titulos = soup.select("span.titleline a")

print("TITULARES DE HACKER NEWS")

for i, t in enumerate(titulos[:10], start=1):
    print(f"{i}. {t.text}")
    print(f"{t['href']}\n")
