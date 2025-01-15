import json

import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather_data(city):
    try:
        response = requests.get('https://api.openweathermap.org/data/2.5/weather',
                                params={
                                    'q': city,
                                    'appid': 'ba87d01c0f415097350cf31874ad33c9',
                                    'units': 'metric'
                                }
                                )
    except Exception as e:
        raise Exception(f'{e}')
    return json.dumps(response.json(), indent=4)


print(get_weather_data('Tashkent'))
print(get_weather_data('London'))
