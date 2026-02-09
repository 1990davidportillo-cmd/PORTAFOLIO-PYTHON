import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://news.ycombinator.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, features="html.parser")

titulos = soup.select("span.titleline a")

nombres = []
enlaces = []

for i, t in enumerate(titulos[:10], start=1):
    nombres.append(t.text)
    enlaces.append(t['href'])

df = pd.DataFrame({
    "Titular": nombres,
    "Enlaces": enlaces
})

print("TITULARES DE HACKER NEWS")
print(df.to_string(index=False))

df.to_excel("Ejemplo pandas.xlsx", index=False)
