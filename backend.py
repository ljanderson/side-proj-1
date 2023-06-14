import requests
import json

api_key = '0aa1f501bd154cc19b604300231406'

city = input('Enter city name: ')

url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data['current']['condition']['text'])
    print(data['location']['lon'])
else:
    print('Error fetching weather data')