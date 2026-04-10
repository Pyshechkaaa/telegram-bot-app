import asyncio
import os
from aiogram import Bot, Dispatcher, types

TOKEN = os.getenv("8667775358:AAEGTOTAoEmZsuQLE54eA60OQXqTCIbLTTM")

if not TOKEN:
    raise Exception("8667775358:AAEGTOTAoEmZsuQLE54eA60OQXqTCIbLTTM is missing")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def start(message: types.Message):
    await message.answer("бот работает 🚀")

async def main():
    print("BOT STARTED")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
