import html
import logging
import os

from aiogram.types import FSInputFile

from aiogram import Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram_bot.keybords.inline_button import get_inline_keyboard

from aiogram_bot.keybords.start_button import reply_keyboard

from services.crypto_news import all_crypto_news
from services.ticker_data import get_crypto_price

from aiogram import Bot
from services.crypto_plot import plot_ticker


# @dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f'Здравства,{message.from_user.first_name}! Голова это ты!',
                         reply_markup=reply_keyboard)


# @dp.message(Command("contacts"))
async def cmd_news(message: types.Message):
    for i in all_crypto_news():
        text_news = f'<b>{(i[1])}</b> \n  {i[2]}  \n  {i[3]}'
        await message.answer(text_news, parse_mode=ParseMode.HTML)


async def interval_news(bot: Bot):
    for i in all_crypto_news():
        text_news = f'{i[1]} \n <b>{i[2]}</b> \n {i[3]}'
        await bot.send_message(chat_id=899967585, text=text_news, parse_mode=ParseMode.HTML)


async def cmd_catalog(message: types.Message):
    await message.answer(text="Каталог", reply_markup=get_inline_keyboard(["111", "222"]))


async def cmd_ticker_price(message: types.Message):
    try:
        message_text = message.text.strip().lower()
        symbol = message_text.split(' ')[1]
        exchange_id = message_text.split(' ')[2]
        price = get_crypto_price(symbol, exchange_id)
        response = f"Курс {symbol} = {price}"
    except:
        logging.error(f"ошибка при запросе цены криптовалюты")
        response = "Произошла ошибка при запросе курса"
    await message.answer(response)


async def cmd_ticker_plot(message: types.Message):
    try:
        plot_ticker('okx', 3, 'LINK/USDT', '15m', '2024-12-3100:00:00Z', 1000)
        ph = FSInputFile(".\\plot.png")
        await message.answer_photo(photo=ph)
    except:
        logging.error(f"ошибка при запросе графика")
        ph = FSInputFile("handlers\\error.png")
        await message.answer_photo(photo=ph)


def register_handlers_client(dp: Dispatcher):
    dp.message.register(cmd_start, Command(commands=['start']))
    dp.message.register(cmd_news, F.text == 'Новости')
    dp.message.register(cmd_ticker_price, lambda message: message.text.strip().lower().startswith('курс '))
    dp.message.register(cmd_ticker_plot, lambda message: message.text.strip().lower().startswith('график'))
