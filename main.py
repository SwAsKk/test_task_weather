import requests

class WeatherDTO:
    def __init__(self, temperature, feels_like, condition):
        self.temperature = temperature
        self.feels_like = feels_like
        self.condition = condition

def get_current_weather():
    location = 'Moscow'
    api_key='foobarkey'
    url = f'https://api.m3o.com/v1/weather/now?location={location}'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print('Smth went wrong i guess..')
        return None

    json_data = response.json()

    # parse the JSON response into a WeatherDTO object
    temperature = json_data['temp_c']
    feels_like = json_data['feels_like_c']
    condition = json_data['condition']

    weather_dto = WeatherDTO(temperature, feels_like, condition)

    return weather_dto

if __name__ == '__main__':
    get_current_weather()