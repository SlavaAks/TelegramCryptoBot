import asyncio

from aiogram_bot.handlers import client
from aiogram_bot.create_bot import bot, dp

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers.client import interval_news


async def start_bot():
    client.register_handlers_client(dp)
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(interval_news, trigger='interval', seconds=600, kwargs={'bot': bot})
    scheduler.start()
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start_bot())
