import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
import asyncio
import re


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

def clear_input() -> dict[str] | None:
    raw_input: str = input()

    normalized_input: str = re.sub(r"[.,;|+]", " ", raw_input)
    raw_words = normalized_input.split()

    clean_words = [
        word.strip().lower() 
        for word in raw_words 
        if len(word.strip()) > 1
    ]

    return clean_words

async def main():
    search_input = clear_input()
    if search_input == None:
        return "Неверный ввод"
    else:
        return "Начинаю следующий шаг"


asyncio.run(main())