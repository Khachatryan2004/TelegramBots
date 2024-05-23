from aiogram import Bot, Dispatcher, executor, types
import aiohttp
import re

token = '6254969627:AAHpIbz7V0zfxjFwaEOhlRCJzl_5Y23i81o'

bot = Bot(token=token)
dp = Dispatcher(bot)


async def download(url):
    async with aiohttp.ClientSession() as session:
        request_url = f'https://api.douyin.wtf/api?url={url}'
        async with session.get(request_url) as response:
            data = await response.json()
            video = data['video_data']['nwm_video_url_HQ']
            return video


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Привет! Чтобы скачать видео, просто отправь на него видео.')


@dp.message_handler()
async def process(message: types.Message):
    if re.compile('https://[a-zA-Z]+.tiktok.com/').match(message.text):
        m = await message.reply('Ожидайте..')
        video = await download(message.text)
        await bot.delete_message(message.chat.id, m['message_id'])
        await message.answer_video(video, caption=f'Готово!')


if __name__ == "__main__":
    executor.start_polling(dp)
