import requests

tulos = requests.get('https://api.chucknorris.io/jokes/random').json()
print(tulos['value'])