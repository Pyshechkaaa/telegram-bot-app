import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise Exception("BOT_TOKEN is missing")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 👉 ссылка на твой Mini App (Render)
WEBAPP_URL = "https://telegram-app-dp2l.onrender.com"

@dp.message()
async def start(message: types.Message):

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🚀 Открыть Mini App",
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        ]
    ])

    await message.answer(
        "Привет 👋\nНажми кнопку чтобы открыть приложение:",
        reply_markup=keyboard
    )


async def main():
    print("BOT STARTED")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
