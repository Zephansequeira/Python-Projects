import os 
from dotenv import find_dotenv, load_dotenv
import requests
import json 
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)




WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1"
MY_LAT = 19.053074559657887
MY_LNG = 72.82850064113481
def get_weather():
  params = {
    "key": WEATHER_API_KEY,
    "q" : "Mumbai" #f'{MY_LAT},{MY_LNG}'
  }
  response = requests.get(f'{BASE_URL}/current.json', params=params)
  return response.json()
def weather_info(data):
  weather_info = {
    "location" : f'{data['location']['name']},{data['location']['country']}',
    "Temp" : f'{data['current']['temp_c']}°C' ,
    "Humidity": f'{data['current']['humidity']}',
    "Rain":f'{data['current']['chance_of_rain']}' ,
  }
  return weather_info
def store_info(data):
  base_dir = os.path.dirname(os.path.abspath(__file__))
  with open(f'{base_dir}\weather.json', "w") as file:
    json.dump(data,file)


data = get_weather()
weather_info = weather_info(data)
print(weather_info)
store_info(weather_info)



