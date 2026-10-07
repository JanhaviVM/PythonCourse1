
# below loads env variables from .env into os.environ, so we can access api keys securely, without hardcding them
from dotenv import load_dotenv
# below formats complex python structures into readable format
from pprint import pprint
# below helps send http requests to web apis and fetch online resources
import requests
# provides built-in os interactions, such as reading env variables loaded by dotenv
# (only after dotenv has made them available within the python program memory called os.environ that python maintans for running processes)
import os

load_dotenv()

# then we define our git current weather function


def get_current_weather(city="Mumbai"):
    print(f'Welcome to the city {city}')
    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == "__main__":
    print(f'\n***Get Current Weather Conditions***\n')
    city = input("Please enter a city name: ")

    # Check for empty string, or string with only spaces
    if not bool(city.strip()):
        city = "Bengaluru"
    weather_data = get_current_weather(city)
    pprint(f'\n{weather_data}')

# upon entering gibberish we get following three lines in terminal
# Please enter a city name: dsdddsdsd
# Welcome to the city dsdddsdsd
# "\n{'cod': '404', 'message': 'city not found'}"

# IMPORTANT: WEATHER.PY IS FOR PRACTICING ON TERMINAL, this is a module, WEBPAGES ARE ON INDEX AND WEATHER HTML FILES, which is the flask app
