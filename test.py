import requests
import json
import time
import const


def get_weather(location):

    url = const.WEATHER_URL.format(city=location,
                                   token=const.WEATHER_TOKEN)
    print(url)
    response = requests.get(url)
    if response.status_code != 200:
        return 'city not found'
    data = json.loads(response.content)
    return parse_weather_data(data)

get_weather('London')
