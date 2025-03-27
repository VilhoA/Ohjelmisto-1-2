import requests
import json

lat = 60.6
lon = 24.8
part = ""
appid = "65509b5468f117ae78d69dcef210c80e"
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&exclude={part}&appid={appid}'

print(url)

tulos = requests.get(url).json()
print(json.dumps(tulos, indent=4))