from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import asyncio
import CONFIG


from aiogram.fsm.storage.redis import RedisStorage

# making redis storage

# use "redis://127.0.0.1:6379" if you running redis local:
storage = RedisStorage.from_url(CONFIG.REDIS_HOST) 

# dispatcher 
dp = Dispatcher(storage=storage)
#bot
bot = Bot(
    token=CONFIG.BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)


async def main():
    

    await dp.start_polling(bot)

# enter point:
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Keyboard interrupt")

