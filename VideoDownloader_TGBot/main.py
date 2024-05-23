from config import tg_bot_token
from aiogram import executor, Dispatcher, types, Bot
import os
from pytube import YouTube
import instaloader

bot = Bot(tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    if last_name:
        full_name = f'{first_name} {last_name}'
    else:
        full_name = first_name

    markup = types.InlineKeyboardMarkup(resize_keyboard=True)
    button1 = types.InlineKeyboardButton(text='Instagram', callback_data='instagram')
    button2 = types.InlineKeyboardButton(text='Youtube', callback_data='youtube')
    markup.add(button1, button2)
    await message.answer(f'Hello dear {full_name}! Glad to see you with us.\n'
                         f'I can download any videos from Instagram and YouTube.\n'
                         f'Just choose the platform you want to download from using the buttons below.',
                         reply_markup=markup)


@dp.callback_query_handler(lambda callback_query: callback_query.data in ['instagram', 'tiktok', 'youtube'])
async def process_platform(callback_query: types.CallbackQuery):
    platform = callback_query.data
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.answer(f'You choose {platform}. Please send me the video URL.')


@dp.message_handler(lambda message: message.text.startswith("http") or message.text.startswith('www'))
async def youtube_download(message: types.Message):
    video_url = message.text

    try:
        yt = YouTube(video_url)
    except Exception as e:
        await message.reply(f"Произошла ошибка при обработке видео: {str(e)}")
        return

    streams = yt.streams

    for stream in streams:
        print(stream)

    output_path = 'Downloaded_Videos'
    os.makedirs(output_path, exist_ok=True)

    try:
        highest_resolution_stream = yt.streams.get_highest_resolution()
        highest_resolution_stream.download(output_path=output_path)
        video_file_path = f'{output_path}/{yt.title}.mp4'
    except Exception as e:
        await message.reply(f"Произошла ошибка при скачивании видео: {str(e)}")
        return

    with open(video_file_path, 'rb') as video_file:
        await bot.send_video(message.chat.id, video=video_file)


if __name__ == '__main__':
    executor.start_polling(dp)
