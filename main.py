import requests
import pandas as pd



api_key = "9923632a83ce5c40a3d7369c3d2f53e7"


url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"


def get_weather(city):
    city_url = url.format(city, api_key)
    response = requests.get(city_url)
    if response.status.code == 200:
        weather_data = pd.json_normalize(response.json)
        weather_data = weather_data[['name', 'main_temp', 'main.feels_like', 'weather.main', 'weather.description']]
        weather_data.columns = ['City', 'Tempreture °C', 'Feels like °C', 'Weather', 'Description']
        return weather_data
    else:
        return pd.DataFrame()


city = input("Ведіть місто:")
weather_data = get_weather(city)

if weather_data.empty:
    print('Прогноз не знайдено')
else:
    print(weather_data)
