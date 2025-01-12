import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("redis_host")
BOT_TOKEN = os.getenv("bot_token")

