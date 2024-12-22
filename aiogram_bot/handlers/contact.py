from aiogram.types import Message
from aiogram import Bot

async def get_true_contact(message:Message,bot:Bot):
    await message.answer(f'ты отправил <b>свой<b> контакт.')

async def get_fake_contact(message:Message,bot:Bot):
    await message.answer(f'ты отправил <b>не свой<b> контакт.')