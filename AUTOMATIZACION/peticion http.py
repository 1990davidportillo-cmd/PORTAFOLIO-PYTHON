import requests

url = "https://news.ycombinator.com/"
respuesta = requests.get(url)

print("Codigo de estado:", respuesta.status_code)

print(respuesta.text[:500])
