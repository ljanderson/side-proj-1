import requests
import json
import datetime

api_key = '0aa1f501bd154cc19b604300231406'

city = input('Enter city name: ')
date = datetime.datetime.now().strftime("%Y-%m-%d")

print(date)

current_url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes'
forecast_url = f'http://api.weatherapi.com/v1/forecast.json?key=0aa1f501bd154cc19b604300231406&q={city}&days=3&aqi=yes&alerts=yes'
astronomy_url = f'http://api.weatherapi.com/v1/astronomy.json?key={api_key}&q={city}&dt={date}'

response = requests.get(current_url)



if response.status_code == 200:
    data = response.json()
    
    #idk where to put these but I defined the "most important" statistics and put them to vairables from the dict
    #youll have to show me how to organize it efficiently

    condition = (data['current']['condition']['text'])
    lon = (data['location']['lon'])
    lat = (data['location']['lat'])
    localtime = (data['location']['localtime'])
    temp_f = (data['current']['temp_f'])
    temp_c = (data['current']['temp_c'])
    
    print(condition)
    print(localtime)
    print(temp_f)
    print(temp_c)

else:
    print('Error fetching weather data')