from config import open_weather_token, tg_bot_token
import datetime
import requests
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    if last_name:
        full_name = f'{first_name} {last_name}'
    else:
        full_name = first_name
    await message.answer(
        f"Hello {full_name}, write the name of any city and I will show you what the weather is like there now.")


@dp.message_handler()
async def get_weather(message: types.Message):
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
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
        )
        data = r.json()

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

        await message.answer(
            f'***{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}***\n'
            f'\nWeather in the city: {city}\nTemperature: {cur_weather}C° {wd}'
            f'\nHumidity: {humidity}%\nPressure: {pressure} mmHg'
            f'\nWind: {wind}\nSunrise: {sunrise_timestamp}'
            f'\nSunset: {sunset_timestamp}'
            f'\nDuration of the day: {length_of_the_day}'
            '\n***Have a good Day!***')

    except:
        await message.reply('\U00002620 Check the city name \U00002620')

    if message.text.isdigit():
        await message.reply('\U00002620 Check the city name \U00002620')
        return


if __name__ == '__main__':
    executor.start_polling(dp)
