import requests
import json

city = input('Syötä kaupunki jonka säätiedot haluat: ')
appid = input('syötä API avain: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units=metric'

#print(url)

tulos = requests.get(url).json()
print(json.dumps(tulos, indent=4))
kuvaus=(json.dumps(tulos['weather'][0]['description']))
asteetc=(json.dumps(tulos['main']['temp']))

print(f'Sää kohteessa on {asteetc} astetta ja {kuvaus}')
print(f'The weather is {asteetc} degrees celcius and {str(kuvaus)}')