import requests
import json

city = 'espoo'
appid = "65509b5468f117ae78d69dcef210c80e"
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units=metric'

#print(url)

tulos = requests.get(url).json()
print(json.dumps(tulos, indent=4))