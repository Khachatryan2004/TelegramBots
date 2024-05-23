import telebot
from telebot import types
import requests

bot = telebot.TeleBot('6095270561:AAGYkzGwT6Vo8AIm30G9fR3epK7n3tPlavs')
amount = 0


@bot.message_handler(commands=['start'])
def start(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    if last_name:
        full_name = f'{first_name} {last_name}'
    else:
        full_name = first_name
    bot.send_message(message.chat.id,
                     f"Hello {full_name}, and welcome to the Currency Conversion Bot! This bot allows you to convert currencies using up-to-date exchange rates. Here's how it works:\n\n"
                     f"1. Enter the amount you wish to convert.\n\n"
                     f"2. Once you enter a valid amount, you will be presented with a selection of currency pairs to choose from and an option to select other currency pairs.\n\n"
                     f"3. Select a currency pair by clicking on the corresponding button. The bot will fetch the current exchange rate from an API and calculate the converted value based on the amount you entered.\n\n"
                     f"4. The bot will display the converted value and allow you to re-enter the amount for further conversions.\n\n"
                     f"This is my first bot, and I hope you'll like it!\n\n"
                     f"Now just write the amount to convert🖋",
                     )


def summa(message):
    global amount
    if message.text.strip() == '/start':
        start(message)
        return
    try:
        amount = float(message.text.strip())
        if amount > 0:
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton('🇺🇸USD/EUR🇪🇺', callback_data='usd/eur')
            button2 = types.InlineKeyboardButton('🇪🇺EUR/USD🇺🇸', callback_data='eur/usd')
            button3 = types.InlineKeyboardButton('🇺🇸USD/RUB🇷🇺', callback_data='usd/rub')
            button4 = types.InlineKeyboardButton('🇷🇺RUB/USD🇺🇸', callback_data='rub/usd')
            button5 = types.InlineKeyboardButton('🇪🇺EUR/RUB🇷🇺', callback_data='eur/rub')
            button6 = types.InlineKeyboardButton('🇷🇺RUB/EUR🇪🇺', callback_data='rub/eur')
            button7 = types.InlineKeyboardButton('🇺🇸USD/AMD🇦🇲', callback_data='usd/amd')
            button8 = types.InlineKeyboardButton('🇦🇲AMD/USD🇺🇸', callback_data='amd/usd')
            button9 = types.InlineKeyboardButton('🇪🇺EUR/AMD🇦🇲', callback_data='eur/amd')
            button10 = types.InlineKeyboardButton('🇦🇲AMD/EUR🇪🇺', callback_data='amd/eur')
            button11 = types.InlineKeyboardButton('List Of Currencies💱', callback_data='list')
            markup.row(button11)
            button12 = types.InlineKeyboardButton('Other Currencies', callback_data='else')
            button13 = types.InlineKeyboardButton('Write your Currency', callback_data='write_currency')
            button14 = types.InlineKeyboardButton('Change Amount💵', callback_data='change')
            markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                       button12, button13, button14)
            bot.send_message(message.chat.id, 'SELECT CURRENCY PAIR OR WRITE ⬇️', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Amount must be greater than 0! Try again')
            bot.register_next_step_handler(message, summa)
    except ValueError:
        bot.send_message(message.chat.id, 'Oops, something is wrong. Try again')
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'else':
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton('🇺🇸USD/UAH🇺🇦', callback_data='usd/uah')
        button2 = types.InlineKeyboardButton('🇺🇦UAH/USD🇺🇸', callback_data='uah/usd')
        button3 = types.InlineKeyboardButton('🇪🇺EUR/UAH🇺🇦', callback_data='eur/uah')
        button4 = types.InlineKeyboardButton('🇺🇦UAH/EUR🇪🇺', callback_data='uah/eur')
        button5 = types.InlineKeyboardButton('🇺🇦UAH/RUB🇷🇺', callback_data='uah/rub')
        button6 = types.InlineKeyboardButton('🇷🇺RUB/UAH🇺🇦', callback_data='rub/uah')
        button7 = types.InlineKeyboardButton('🇺🇸USD/GBP🇬🇧󠁧󠁢󠁥󠁮󠁧󠁿', callback_data='usd/gbp')
        button8 = types.InlineKeyboardButton('🇬🇧󠁧󠁢󠁥󠁮󠁧󠁿GBP/USD🇺🇸', callback_data='gbp/usd')
        button9 = types.InlineKeyboardButton('🇪🇺EUR/GBP🇬🇧', callback_data='eur/gbp')
        button10 = types.InlineKeyboardButton('🇬🇧󠁧󠁢󠁥󠁮󠁧󠁿GBP/EUR🇪🇺', callback_data='gbp/eur')
        button11 = types.InlineKeyboardButton('Back', callback_data='back')
        button12 = types.InlineKeyboardButton('Write your Currency', callback_data='write_currency')
        button13 = types.InlineKeyboardButton('Change Amount💵', callback_data='change')
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                   button11, button12, button13)
        bot.send_message(call.message.chat.id, 'SELECT CURRENCY PAIR OR WRITE ⬇️', reply_markup=markup)
    elif call.data == 'list':
        bot.send_message(call.message.chat.id, 'Armenia 🇦🇲 - AMD,   '
                                               'Australia 🇦🇺 - AUD,   '
                                               'Austria 🇦🇹 - EUR,   '
                                               'Azerbaijan 🇦🇿 - AZN,   '
                                               'Bangladesh 🇧🇩 - BDT,   '
                                               'Belgium 🇧🇪 - EUR,   '
                                               'Brazil 🇧🇷 - BRL,   '
                                               'Bulgaria 🇧🇬 - BGN,   '
                                               'Canada 🇨🇦 - CAD,   '
                                               'China 🇨🇳 - CNY,   '
                                               'Croatia 🇭🇷 - HRK,   '
                                               'Cyprus 🇨🇾 - EUR,   '
                                               'Czech 🇨🇿 - CZK,   '
                                               'Denmark 🇩🇰 - DKK,   '
                                               'Egypt 🇪🇬 - EGP,   '
                                               'Estonia 🇪🇪 - EUR,   '
                                               'Finland 🇫🇮 - EUR,   '
                                               'France 🇫🇷 - EUR,   '
                                               'Germany 🇩🇪 - EUR,   '
                                               'Greece 🇬🇷 - EUR,   '
                                               'Hungary 🇭🇺 - HUF,   '
                                               'Iceland 🇮🇸 - ISK,   '
                                               'India 🇮🇳 - INR,   '
                                               'Indonesia 🇮🇩 - IDR,   '
                                               'Iran 🇮🇷 - IRR,   '
                                               'Iraq 🇮🇶 - IQD,   '
                                               'Ireland 🇮🇪 - EUR,   '
                                               'Israel 🇮🇱 - ILS,   '
                                               'Italy 🇮🇹 - EUR,   '
                                               'Japan 🇯🇵 - JPY,   '
                                               'Jordan 🇯🇴 - JOD,   '
                                               'Kazakhstan 🇰🇿 - KZT,   '
                                               'Kenya 🇰🇪 - KES,   '
                                               'Kuwait 🇰🇼 - KWD,   '
                                               'Lebanon 🇱🇧 - LBP,   '
                                               'Malaysia 🇲🇾 - MYR,   '
                                               'Mexico 🇲🇽 - MXN,   '
                                               'Netherlands 🇳🇱 - EUR,   '
                                               'New Zealand 🇳🇿 - NZD,   '
                                               'Nigeria 🇳🇬 - NGN,   '
                                               'Norway 🇳🇴 - NOK,   '
                                               'Pakistan 🇵🇰 - PKR,   '
                                               'Philippines 🇵🇭 - PHP,   '
                                               'Poland 🇵🇱 - PLN,   '
                                               'Portugal 🇵🇹 - EUR,   '
                                               'Qatar 🇶🇦 - QAR,   '
                                               'Romania 🇷🇴 - RON,   '
                                               'Russia 🇷🇺 - RUB,   '
                                               'Saudi Arabia 🇸🇦 - SAR,   '
                                               'Serbia 🇷🇸 - RSD,   '
                                               'Singapore 🇸🇬 - SGD,   '
                                               'Slovakia 🇸🇰 - EUR,   '
                                               'Slovenia 🇸🇮 - EUR,   '
                                               'South Africa 🇿🇦 - ZAR,   '
                                               'South Korea 🇰🇷 - KRW,   '
                                               'Spain 🇪🇸 - EUR,   '
                                               'Sweden 🇸🇪 - SEK,   '
                                               'Switzerland 🇨🇭 - CHF,   '
                                               'Taiwan 🇹🇼 - TWD,   '
                                               'Thailand 🇹🇭 - THB,   '
                                               'Turkey 🇹🇷 - TRY,   '
                                               'Ukraine 🇺🇦 - UAH,   '
                                               'United Arab Emirates 🇦🇪 - AED,   '
                                               'United Kingdom 🇬🇧 - GBP,   '
                                               'United States 🇺🇸 - USD,   '
                                               'Vietnam 🇻🇳 - VND   '
                         )
    elif call.data == 'change':
        bot.send_message(call.message.chat.id, 'Write the new Amount')
        bot.register_next_step_handler(call.message, summa)
    elif call.data == 'back':
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton('🇺🇸USD/EUR🇪🇺', callback_data='usd/eur')
        button2 = types.InlineKeyboardButton('🇪🇺EUR/USD🇺🇸', callback_data='eur/usd')
        button3 = types.InlineKeyboardButton('🇺🇸USD/RUB🇷🇺', callback_data='usd/rub')
        button4 = types.InlineKeyboardButton('🇷🇺RUB/USD🇺🇸', callback_data='rub/usd')
        button5 = types.InlineKeyboardButton('🇪🇺EUR/RUB🇷🇺', callback_data='eur/rub')
        button6 = types.InlineKeyboardButton('🇷🇺RUB/EUR🇪🇺', callback_data='rub/eur')
        button7 = types.InlineKeyboardButton('🇺🇸USD/AMD🇦🇲', callback_data='usd/amd')
        button8 = types.InlineKeyboardButton('🇦🇲AMD/USD🇺🇸', callback_data='amd/usd')
        button9 = types.InlineKeyboardButton('🇪🇺EUR/AMD🇦🇲', callback_data='eur/amd')
        button10 = types.InlineKeyboardButton('🇦🇲AMD/EUR🇪🇺', callback_data='amd/eur')
        button11 = types.InlineKeyboardButton('List Of Currencies💱', callback_data='list')
        markup.row(button11)
        button12 = types.InlineKeyboardButton('Other Currencies', callback_data='else')
        button13 = types.InlineKeyboardButton('Write your Currency', callback_data='write_currency')
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                   button12, button13)
        bot.send_message(call.message.chat.id, 'SELECT CURRENCY PAIR OR WRITE ⬇️', reply_markup=markup)

    elif call.data == 'write_currency':
        bot.send_message(call.message.chat.id,
                         'Please enter your currency pair in the following format: Currency1/Currency2\n|Example: USD/EUR')
        bot.register_next_step_handler(call.message, custom_currency)
    else:
        values = call.data.upper().split('/')
        if len(values) == 2:
            currency1, currency2 = values
            url = f'https://api.exchangerate-api.com/v4/latest/{values[0]}'
            response = requests.get(url)
            data = response.json()
            if values[1] in data['rates']:
                rate = data['rates'][values[1]]
                res = amount * rate
                bot.send_message(call.message.chat.id, f'Value: {round(res, 2)}. Re-enter the amount')
                bot.register_next_step_handler(call.message, summa)
            else:
                bot.send_message(call.message.chat.id, 'Invalid Currency. Please try again.')
        else:
            bot.send_message(call.message.chat.id, 'Invalid Currency pair. Please try again.')


def custom_currency(message):
    try:
        currency_pair = message.text.strip()
        currency_pair = currency_pair.replace('/', '-')
        base_currency, target_currency = currency_pair.split('-')

        base_currency = base_currency.upper()
        target_currency = target_currency.upper()

        url = f'https://api.exchangerate-api.com/v4/latest/{base_currency}'
        response = requests.get(url)
        data = response.json()

        if target_currency.upper() in data['rates']:
            exchange_rate = data['rates'][target_currency.upper()]
            converted_amount = round(amount * exchange_rate, 2)
            bot.send_message(message.chat.id, f'{amount} {base_currency} = {converted_amount} {target_currency}')
        else:
            bot.send_message(message.chat.id, 'Invalid Currency pair. Please try again.')

        bot.send_message(message.chat.id, 'Enter the new Amount to convert or use the buttons',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Something is wrong, start the bot again or click any button')


bot.polling(none_stop=True)
