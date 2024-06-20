import asyncio
import logging

from config import *
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters.command import Command

logging.basicConfig(filename='logs/napominalka.log',
                    encoding='utf-8',  level=logging.DEBUG)
bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message):
    await bot.send_message(chat_id=message.chat.id, text='Hello')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
