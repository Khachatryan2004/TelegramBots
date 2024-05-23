from aiogram import Bot, Dispatcher, executor, types
from config import tg_bot_token
import requests
import pyshorteners
from bs4 import BeautifulSoup

bot = Bot(tg_bot_token)
dp = Dispatcher(bot)
s = pyshorteners.Shortener()


@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    if last_name:
        full_name = f'{first_name} {last_name}'
    else:
        full_name = first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Առաքման պայմաններ')
    button2 = types.KeyboardButton(text='Դիտել տեսականին')
    markup.add(button1, button2)

    await message.answer(
        f"Բարև Ձեզ {full_name} ջան☺️\nԸնտրեք Ձեր ցանկացաց տեսականին", reply_markup=markup)


@dp.message_handler(lambda message: message.text == 'Դիտել տեսականին')
async def show_category_buttons(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Ականջօղ')
    button2 = types.KeyboardButton(text='Ոտքի շղթա')
    button3 = types.KeyboardButton(text='ՔաՖՖ')
    button4 = types.KeyboardButton(text='Թևնոց')
    button5 = types.KeyboardButton(text='Վզնոց')
    button6 = types.KeyboardButton(text='Նվեր քարտ')
    button7 = types.KeyboardButton(text='Վերադառնալ հետ')
    markup.add(button1, button2, button3, button4, button5, button6, button7)
    await message.answer("Ընտրեք տեսականին:", reply_markup=markup)


@dp.message_handler(lambda message: message.text == 'Առաքման պայմաններ')
async def show_delivery_conditions(message: types.Message):
    await message.answer('Փոստային: 2-5 աշխ. օր 500 ֏\nԱռաքիչի միջոցով: Վճարման հաջորդ օրը 1000 ֏')


@dp.message_handler(lambda message: message.text == 'Վերադառնալ հետ')
async def back_function(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Առաքման պայմաններ')
    button2 = types.KeyboardButton(text='Դիտել տեսականին')
    markup.add(button1, button2)
    await message.answer('Դուք վերադառձաք հետ', reply_markup=markup)


@dp.message_handler(lambda message: message.text in ['Ականջօղ', 'Ոտքի շղթա', 'ՔաՖՖ', 'Թևնոց', 'Վզնոց'])
async def colors(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Արծաթագույն')
    button2 = types.KeyboardButton(text='Ոսկեգույն')
    button3 = types.KeyboardButton(text='Վարդագույն ոսկի')
    button4 = types.KeyboardButton(text='Ամբողջը')
    markup.add(button1, button2, button3, button4)
    await message.answer('Ընրեք Գույնը', reply_markup=markup)


@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == 'Ականջօղ':
            pass
        elif message.text == 'Արծաթագույն':
            url = 'https://shinyme.am/hy/product_cat/earring/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find_all('ul', class_='product_list')
            for products in section:
                product = products.find_all('li', class_='product')
                for item in product:
                    product_colors = item.find('ul', class_='product_colors')
                    product_color = product_colors.find('li')['title']

                    product_name = item.find('h2', class_="product_title").get_text(strip=True)
                    product_image = item.find('div', class_='product_image')
                    product_link = product_image.find('a')['href']
                    product_original_price = item.find('span', class_='original_price')
                    product_discounted_price = item.find('span', class_='final_price discounted')
                    product_final_price = item.find('span', class_='final_price')

                    if product_original_price and product_discounted_price:
                        orig_price = product_original_price.get_text(strip=True).replace('֏', '').replace(',', '')
                        orig_price = int(orig_price)
                        disc_price = product_discounted_price.get_text(strip=True).replace('֏', '').replace(',', '')
                        disc_price = int(disc_price)

                    else:
                        orig_price = None
                        disc_price = None

                    if product_final_price:
                        final_price = product_final_price.get_text(strip=True).replace('֏', '').replace(',', '')
                        final_price = int(final_price)
                    else:
                        final_price = None

                    if product_original_price is not None and product_discounted_price is not None:
                        short_link = s.tinyurl.short(product_link)
                        await message.answer(
                            f'{product_name}\n Old Price:{orig_price}\n New Price:{disc_price}\n Link:{short_link}')

                    elif product_final_price is not None:
                        short_link = s.tinyurl.short(product_link)
                        await message.answer(f'{product_name}\n Price:{final_price}\n Link:{short_link}')
                    else:

                        short_link = s.tinyurl.short(product_link)
                        await message.answer(f'{product_name}\n Link:{short_link}')

        if message.text == 'Ոտքի շղթա':

            url = 'https://shinyme.am/hy/product_cat/anklet/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find_all('ul', class_='product_list')
            for products in section:
                product = products.find_all('li', class_='product')
                for item in product:

                    product_name = item.find('h2', class_="product_title").get_text(strip=True)
                    product_image = item.find('div', class_='product_image')
                    product_link = product_image.find('a')['href']
                    product_original_price = item.find('span', class_='original_price')
                    product_discounted_price = item.find('span', class_='final_price discounted')
                    product_final_price = item.find('span', class_='final_price')

                    if product_original_price and product_discounted_price:
                        orig_price = product_original_price.get_text(strip=True).replace('֏', '').replace(',', '')
                        orig_price = int(orig_price)
                        disc_price = product_discounted_price.get_text(strip=True).replace('֏', '').replace(',', '')
                        disc_price = int(disc_price)

                    else:
                        orig_price = None
                        disc_price = None

                    if product_final_price:
                        final_price = product_final_price.get_text(strip=True).replace('֏', '').replace(',', '')
                        final_price = int(final_price)
                    else:
                        final_price = None

                    if product_original_price is not None and product_discounted_price is not None:
                        short_link = s.tinyurl.short(product_link)
                        await message.answer(
                            f'{product_name}\n Old Price:{orig_price}\n New Price:{disc_price}\n Link:{short_link}')

                    elif product_final_price is not None:
                        short_link = s.tinyurl.short(product_link)
                        await message.answer(f'{product_name}\n Price:{final_price}\n Link:{short_link}')
                    else:

                        short_link = s.tinyurl.short(product_link)
                        await message.answer(f'{product_name}\n Link:{short_link}')

        if message.text == 'ՔաՖՖ':

            url = 'https://shinyme.am/hy/product_cat/cuff/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find_all('ul', class_='product_list')
            for products in section:
                product = products.find_all('li', class_='product')
                for item in product:
                    product_name = item.find('h2', class_="product_title").get_text(strip=True)
                    product_image = item.find('div', class_='product_image')
                    product_link = product_image.find('a')['href']
                    product_original_price = item.find('span', class_='original_price')
                    product_discounted_price = item.find('span', class_='final_price discounted')
                    product_final_price = item.find('span', class_='final_price')

                    if product_original_price and product_discounted_price:
                        orig_price = product_original_price.get_text(strip=True).replace('֏', '').replace(',', '')
                        orig_price = int(orig_price)
                        disc_price = product_discounted_price.get_text(strip=True).replace('֏', '').replace(',', '')
                        disc_price = int(disc_price)

                    else:
                        orig_price = None
                        disc_price = None

                    if product_final_price:
                        final_price = product_final_price.get_text(strip=True).replace('֏', '').replace(',', '')
                        final_price = int(final_price)
                    else:
                        final_price = None

                    if product_original_price is not None and product_discounted_price is not None:
                        short_link = s.tinyurl.short(product_link)
                        await message.answer(
                            f'{product_name}\n Old Price:{orig_price}\n New Price:{disc_price}\n Link:{short_link}')

                    elif product_final_price is not None:
                        short_link = s.tinyurl.short(product_link)
                        await message.answer(f'{product_name}\n Price:{final_price}\n Link:{short_link}')
                    else:

                        short_link = s.tinyurl.short(product_link)
                        await message.answer(f'{product_name}\n Link:{short_link}')

        if message.text == 'Թևնոց':

            url = 'https://shinyme.am/hy/product_cat/bracelet/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find_all('ul', class_='product_list')
            for products in section:
                product = products.find_all('li', class_='product')
                for item in product:
                    product_name = item.find('h2', class_="product_title").get_text(strip=True)
                    product_image = item.find('div', class_='product_image')
                    product_link = product_image.find('a')['href']
                    product_original_price = item.find('span', class_='original_price')
                    product_discounted_price = item.find('span', class_='final_price discounted')
                    product_final_price = item.find('span', class_='final_price')

                    if product_original_price and product_discounted_price:
                        orig_price = product_original_price.get_text(strip=True).replace('֏', '').replace(',', '')
                        orig_price = int(orig_price)
                        disc_price = product_discounted_price.get_text(strip=True).replace('֏', '').replace(',', '')
                        disc_price = int(disc_price)

                    else:
                        orig_price = None
                        disc_price = None

                    if product_final_price:
                        final_price = product_final_price.get_text(strip=True).replace('֏', '').replace(',', '')
                        final_price = int(final_price)
                    else:
                        final_price = None

                    if product_original_price is not None and product_discounted_price is not None:
                        short_link = s.tinyurl.short(product_link)
                        await message.answer(
                            f'{product_name}\n Old Price:{orig_price}\n New Price:{disc_price}\n Link:{short_link}')

                    elif product_final_price is not None:
                        short_link = s.tinyurl.short(product_link)
                        await message.answer(f'{product_name}\n Price:{final_price}\n Link:{short_link}')
                    else:

                        short_link = s.tinyurl.short(product_link)
                        await message.answer(f'{product_name}\n Link:{short_link}')

        if message.text == 'Վզնոց':

            url = 'https://shinyme.am/hy/product_cat/necklace/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find_all('ul', class_='product_list')
            for products in section:
                product = products.find_all('li', class_='product')
                for item in product:
                    product_name = item.find('h2', class_="product_title").get_text(strip=True)
                    product_image = item.find('div', class_='product_image')
                    product_link = product_image.find('a')['href']
                    product_original_price = item.find('span', class_='original_price')
                    product_discounted_price = item.find('span', class_='final_price discounted')
                    product_final_price = item.find('span', class_='final_price')

                    if product_original_price and product_discounted_price:
                        orig_price = product_original_price.get_text(strip=True).replace('֏', '').replace(',', '')
                        orig_price = int(orig_price)
                        disc_price = product_discounted_price.get_text(strip=True).replace('֏', '').replace(',', '')
                        disc_price = int(disc_price)

                    else:
                        orig_price = None
                        disc_price = None

                    if product_final_price:
                        final_price = product_final_price.get_text(strip=True).replace('֏', '').replace(',', '')
                        final_price = int(final_price)
                    else:
                        final_price = None

                    if product_original_price is not None and product_discounted_price is not None:
                        short_link = s.tinyurl.short(product_link)
                        await message.answer(
                            f'{product_name}\n Old Price:{orig_price}\n New Price:{disc_price}\n Link:{short_link}')

                    elif product_final_price is not None:
                        short_link = s.tinyurl.short(product_link)
                        await message.answer(f'{product_name}\n Price:{final_price}\n Link:{short_link}')
                    else:

                        short_link = s.tinyurl.short(product_link)
                        await message.answer(f'{product_name}\n Link:{short_link}')


if __name__ == '__main__':
    executor.start_polling(dp)
