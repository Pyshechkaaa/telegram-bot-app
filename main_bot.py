from aiogram import Bot, Dispatcher
import asyncio
import os

bot = Bot(token=os.getenv("8667775358:AAEGTOTAoEmZsuQLE54eA60OQXqTCIbLTTM"))
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

asyncio.run(main())