# we create a program that goes on internet
# requests the weather from a service
# and returns the current weather to us, any city

# First step, goto https://openweathermap.org/ and signup

# when you deploy an application.
# your host will allow you to insert the enviornment variables
# in spaces they have provided on the host for the website for example,
# i.e. you would take the api key value and take it to your host

# on the website, under the tab API, scroll down to "Current Weather Data"
# on that page, thy will provide a URL on which we can request weather data from
# omething like below
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# We will now modify the URL to suit or needs
# instead of lat and lon, we can provide city name
# so on the rigtht hand side of the website's page, click on "Units of Measurement"
# add &unit=metric at theend of the URL below

import requests
# below helps get enviornment variable value
from dotenv import load_dotenv
import os
from pprint import pprint

# this loads in the enviornment variables, so we can retrieve them ( in this case onyl the api key)
# its important to call this first so its avaialble for us
load_dotenv()


def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # print(request_url)

    weather_data = requests.get(request_url).json()

    pprint(weather_data)

    print(f'\nCurrent weather for {weather_data["name"]}:')
    print(f'\nThe temprature is {weather_data["main"]["temp"]}')
    print(
        f'\nFeels like {weather_data["main"]["feels_like"]} & {weather_data["weather"][0]["description"]}.')


if __name__ == "__main__":
    get_current_weather()
