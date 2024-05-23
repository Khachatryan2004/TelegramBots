from aiogram import Bot, Dispatcher, executor, types
from config import tg_bot_token
import requests
import pyshorteners
from bs4 import BeautifulSoup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import hashlib

bot = Bot(tg_bot_token)
dp = Dispatcher(bot)
s = pyshorteners.Shortener()
link = 'https://www.instagram.com/shinyme.am/'


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
    button3 = types.KeyboardButton(text='Shiny փաթեթավորում')
    markup.add(button1, button2)
    markup.add(button3)

    await message.answer(
        f"Բարև Ձեզ {full_name} ջան☺️\nԸնտրեք Ձեր ցանկացաց տեսականին", reply_markup=markup)


@dp.message_handler(commands=['instagram'])
async def instagram(message: types.Message):
    button = InlineKeyboardButton(text="ShinyMe", url="https://www.instagram.com/shinyme.am/")
    keyboard = InlineKeyboardMarkup().add(button)

    await message.answer("Սեղմեք կոճակը՝ Instagram մուտք գործելու համար:", reply_markup=keyboard)


@dp.message_handler(commands=['website'])
async def website(message: types.Message):
    button = InlineKeyboardButton(text="ShinyMe", url="https://shinyme.am/hy/")
    keyboard = InlineKeyboardMarkup().add(button)

    await message.answer("Սեղմեք կոճակը՝ կայք մուտք գործելու համար:", reply_markup=keyboard)


@dp.message_handler(commands=['delivery'])
async def delivery(message: types.Message):
    await message.answer("Փոստային: 2-5 աշխ. օր 500 ֏\nԱռաքիչի միջոցով: Վճարման հաջորդ օրը 1000 ֏")


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


@dp.message_handler(lambda message: message.text == 'Shiny փաթեթավորում')
async def package(message: types.Message):
    photo_url = 'https://shinyme.am/wp-content/uploads/2022/12/packaging_image.png'
    await bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption='Shiny փաթեթավորում\n'
                                                                           'Մեր փայլփլուն բացիկի տեսքով փաթեթավորումը ԱՆՎՃԱՐ է բոլոր պատվերների համար, իսկ վարդագույն տուփն արժե 700դր։'
                                                                           'Ինչպես նաև, բոլոր պատվերների ներսում դրվում են անվանական բացիկներ՝ նվերի հասցեատիրոջ անունով, որպեսզի անհատական լինի ցանկացած նվեր,'
                                                                           'անգամ եթե հենց քեզ համար ես ընտրել։\n\n'
                                                                           'Արի՛ միասին ընդգծենք քո ներքին փայլը։')


@dp.message_handler(lambda message: message.text == 'Վերադառնալ հետ')
async def back_function(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Առաքման պայմաններ')
    button2 = types.KeyboardButton(text='Դիտել տեսականին')
    button3 = types.KeyboardButton(text='Shiny փաթեթավորում')
    markup.add(button1, button2)
    markup.add(button3)
    await message.answer('Դուք վերադառձաք հետ', reply_markup=markup)


# types of products
@dp.message_handler(lambda message: message.text == 'Ականջօղ')
async def earring(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Արծաթագույն ականջօղ')
    button2 = types.KeyboardButton(text='Ոսկեգույն ականջօղ')
    button3 = types.KeyboardButton(text='Վարդագույն ոսկի ականջօղ')
    button4 = types.KeyboardButton(text='Բոլոր ականջօղերը')
    button5 = types.KeyboardButton(text='Վերադառնալ հետ')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    markup.add(button5)
    await message.answer('Ընրեք Գույնը', reply_markup=markup)


@dp.message_handler(lambda message: message.text == 'Ոտքի շղթա')
async def anklet(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Արծաթագույն ոտքի շղթա')
    button2 = types.KeyboardButton(text='Ոսկեգույն ոտքի շղթա')
    button3 = types.KeyboardButton(text='Վարդագույն ոսկի ոտքի շղթա')
    button4 = types.KeyboardButton(text='Բոլոր ոտքի շղթաները')
    button5 = types.KeyboardButton(text='Վերադառնալ հետ')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    markup.add(button5)
    await message.answer('Ընրեք Գույնը', reply_markup=markup)


@dp.message_handler(lambda message: message.text == 'ՔաՖՖ')
async def cuff(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Արծաթագույն քաՖՖ')
    button2 = types.KeyboardButton(text='Ոսկեգույն քաՖՖ')
    button3 = types.KeyboardButton(text='Վարդագույն ոսկի քաՖՖ')
    button4 = types.KeyboardButton(text='Բոլոր քաՖՖերը')
    button5 = types.KeyboardButton(text='Վերադառնալ հետ')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    markup.add(button5)
    await message.answer('Ընրեք Գույնը', reply_markup=markup)


@dp.message_handler(lambda message: message.text == 'Թևնոց')
async def bracelet(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Արծաթագույն թևնոց')
    button2 = types.KeyboardButton(text='Ոսկեգույն թևնոց')
    button3 = types.KeyboardButton(text='Վարդագույն ոսկի թևնոց')
    button4 = types.KeyboardButton(text='Բոլոր թևնոցները')
    button5 = types.KeyboardButton(text='Վերադառնալ հետ')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    markup.add(button5)
    await message.answer('Ընրեք Գույնը', reply_markup=markup)


@dp.message_handler(lambda message: message.text == 'Վզնոց')
async def necklace(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Արծաթագույն վզնոց')
    button2 = types.KeyboardButton(text='Ոսկեգույն վզնոց')
    button3 = types.KeyboardButton(text='Վարդագույն ոսկի վզնոց')
    button4 = types.KeyboardButton(text='Բոլոր վզնոցները ')
    button5 = types.KeyboardButton(text='Վերադառնալ հետ')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    markup.add(button5)
    await message.answer('Ընրեք Գույնը', reply_markup=markup)


async def process_products(message: types.Message, category_name: str, url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    section = soup.find_all('ul', class_='product_list')

    products = []
    for products_list in section:
        product_items = products_list.find_all('li', class_='product')
        for item in product_items:
            product_name = item.find('h2', class_="product_title").get_text(strip=True)
            product_image = item.find('img')
            if product_image:
                product_image_url = product_image['src']
            else:
                product_image_url = "Նկար գոյություն չունի"

            product_link_element = item.find('div', class_='product_image')
            if product_link_element:
                product_link = product_link_element.find('a')['href']
            else:
                product_link = "Հղում գոյություն չունի"

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
                products.append(
                    f"*{product_name}*\n"
                    f"Հին գին: {orig_price} ֏\n"
                    f"Նոր գին: {disc_price} ֏\n"
                    f"Նկարի լինկը: {product_image_url}\n"
                    f"Կայքի լինկը: {product_link}\n\n"
                )
            elif product_final_price is not None:
                products.append(
                    f"*{product_name}*\n"
                    f"Գին: {final_price} ֏\n"
                    f"Նկարի լինկը: {product_image_url}\n"
                    f"Կայքի լինկը: {product_link}\n\n"
                )
            else:
                products.append(
                    f"*{product_name}*\n"
                    f"Նկարի լինկը: {product_image_url}\n"
                    f"Կայքի լինկը: {product_link}\n\n"
                )
    grouped_products = [products[i:i + 1] for i in range(0, len(products), 1)]
    for group in grouped_products:
        products_info = f"{message.text}\n\n"
        products_info += "\n\n".join(group)
        await message.answer(products_info)


@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text in ['Ականջօղ', 'Ոտքի շղթա', 'ՔաՖՖ', 'Թևնոց', 'Վզնոց']:
            pass
        elif message.text in ['Արծաթագույն ականջօղ', 'Ոսկեգույն ականջօղ', 'Վարդագույն ոսկի ականջօղ',
                              'Բոլոր ականջօղերը', 'Արծաթագույն ոտքի շղթա', 'Ոսկեգույն ոտքի շղթա',
                              'Վարդագույն ոսկի ոտքի շղթա', 'Բոլոր ոտքի շղթաները', 'Արծաթագույն քաՖՖ', 'Ոսկեգույն քաՖՖ',
                              'Վարդագույն ոսկի քաՖՖ', 'Բոլոր քաՖՖերը', 'Արծաթագույն թևնոց', 'Ոսկեգույն թևնոց',
                              'Վարդագույն ոսկի թևնոց', 'Բոլոր թևնոցները', 'Արծաթագույն վզնոց', 'Ոսկեգույն վզնոց',
                              'Վարդագույն ոսկի վզնոց', 'Բոլոր վզնոցները']:

            category_name = message.text
            url_mapping = {
                'Արծաթագույն ականջօղ': 'https://shinyme.am/hy/product_cat/earring/?filter[color][]=49&sort=price_asc',
                'Ոսկեգույն ականջօղ': 'https://shinyme.am/hy/product_cat/earring/?filter[color][]=50&sort=price_asc',
                'Բոլոր ականջօղերը': 'https://shinyme.am/hy/product_cat/earring/?sort=price_asc',

                'Արծաթագույն ոտքի շղթա': 'https://shinyme.am/hy/product_cat/anklet/?filter[color][]=49&sort=price_asc',
                'Բոլոր ոտքի շղթաները': 'https://shinyme.am/hy/product_cat/anklet/?sort=price_asc',

                'Արծաթագույն քաՖՖ': 'https://shinyme.am/hy/product_cat/cuff/?filter[color][]=49&sort=price_asc',
                'Ոսկեգույն քաՖՖ': 'https://shinyme.am/hy/product_cat/cuff/?filter[color][]=50&sort=price_asc',
                'Վարդագույն ոսկի քաՖՖ': 'https://shinyme.am/hy/product_cat/cuff/?filter[color][]=51&sort=price_asc',
                'Բոլոր քաՖՖերը': 'https://shinyme.am/hy/product_cat/cuff/?sort=price_asc',

                'Արծաթագույն թևնոց': 'https://shinyme.am/hy/product_cat/bracelet/?filter[color][]=49&sort=price_asc',
                'Բոլոր թևնոցները': 'https://shinyme.am/hy/product_cat/bracelet/?sort=price_asc',

                'Արծաթագույն վզնոց': 'https://shinyme.am/hy/product_cat/necklace/?filter[color][]=49&sort=price_asc',
                'Ոսկեգույն վզնոց': 'https://shinyme.am/hy/product_cat/necklace/?filter[color][]=50&sort=price_asc',
                'Վարդագույն ոսկի վզնոց': 'https://shinyme.am/hy/product_cat/necklace/?filter[color][]=51&sort=price_asc',
                'Բոլոր վզնոցները': 'https://shinyme.am/hy/product_cat/necklace/?sort=price_asc',

            }
            if category_name in url_mapping:
                url = url_mapping[category_name]
                if category_name in ['Վարդագույն ոսկի ականջօղ', 'Ոսկեգույն ոտքի շղթա', 'Վարդագույն ոսկի ոտքի շղթա',
                                     'Ոսկեգույն թևնոց', 'Վարդագույն ոսկի թևնոց']:
                    await message.answer('Տվյալ գույնը հասանելի չէ')
                else:
                    await process_products(message, category_name, url)
            else:
                await message.answer('Տվյալ գույնը հասանելի չէ')
        elif message.text == 'Նվեր քարտ':
            photo_url = 'https://shinyme.am/wp-content/uploads/2022/12/gift_card_image.png'
            await bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'Նվեր քարտ\n\n'
                                 f'Երբ չես կողմնորոշվում՝ որ մոդելը նվիրել, նվեր քարտը լավագույն տարբերակն է!'
                                 f'Մենք չունենք մինիմալ կամ մաքսիմալ գումարի շեմ. պարզապես գրիր մեր ինստագրամի '
                                 f'էջին եւ նշիր նվեր քարտի չափը, որ ցանկանում ես նվիրել։\n{link}')


if __name__ == '__main__':
    executor.start_polling(dp)
