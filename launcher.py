import os
import asyncio
from dotenv import load_dotenv
from bot import Bot

load_dotenv()

async def main():
    bot_token = os.getenv("BOT_TOKEN")
    bot = Bot()
    async with bot:
        await bot.start(bot_token)


asyncio.run(main())