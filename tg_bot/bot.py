from aiogram import Bot, Dispatcher
import asyncio
from dotenv import load_dotenv
import os
from handlers import router as rt

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(rt)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
