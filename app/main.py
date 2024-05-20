import asyncio
from aiogram import Bot, Dispatcher
from routers import pidor_router



async def main():
    bot = Bot(token=API_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(pidor_router.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)




if __name__ == "__main__":
    asyncio.run(main())


