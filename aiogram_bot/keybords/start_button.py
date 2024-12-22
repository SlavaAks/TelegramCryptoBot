from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Биржи'), ],
    [KeyboardButton(text='Новости'),
     KeyboardButton(text='Отчет')]
],
    resize_keyboard=True,
    one_time_keyboard=True)
