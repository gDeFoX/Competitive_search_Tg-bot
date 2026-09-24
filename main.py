from os import getenv
import asyncio
import logging
import sys

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Hello, {html.mono(message.from_user.full_name)}!"
    )


class SearchStates(StatesGroup):
    wating_for_query: State = State()


@dp.message()
async def start_search(message: Message, state: FSMContext) -> None:
    await message.answer("Enter your query:")
    await state.set_state(SearchStates.wating_for_query)


@dp.message(SearchStates.waiting_for_query)
async def process_search_query(message: Message, state: FSMContext) -> None:
    query: str = message.text

    # Код поиска
    await message.answer(f"Searching: {query}")

    await state.clear()


dp.message()
async def echo(message: Message) -> None:
    await message.answer("Send /search for searching")


async def main() -> None:
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())