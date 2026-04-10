import asyncio
import os
from aiogram import Bot, Dispatcher, types

TOKEN = os.getenv("8667775358:AAEGTOTAoEmZsuQLE54eA60OQXqTCIbLTTM")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def start(message: types.Message):
    await message.answer("бот работает 🚀")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
