import requests
from config import open_weather_token
from pprint import pprint
import datetime


def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B"
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        print(
            f'***{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}***\n'
            f'\nWeather in the city: {city}\nTemperature: {cur_weather}C° {wd}'
            f'\nHumdity: {humidity}%\nPressure: {pressure} mmHg'
            f'\nWind: {wind}\nSunrise: {sunrise_timestamp}'
            f'\nSunset: {sunset_timestamp}'
            f'\nDuration of the day: {length_of_the_day}')

    except Exception as ex:
        print(ex)
        print('Check city name')


def main():
    city = input('Enter the city:\t')
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
