import asyncio
import logging
import datetime

from kb import *
from config import *

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.command import Command

logging.basicConfig(filename='logs/napominalka.log',
                    encoding='utf-8',  level=logging.DEBUG)
bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=start1)
    await message.answer("Здравствуйте", reply_markup=kb)


@dp.callback_query(F.data == 'make')
async def start_callback(callback: CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=years)
    await callback.message.edit_text('Выберите год', reply_markup=kb)


@dp.callback_query(F.data == 'months')
async def years_callback(callback: CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=months)
    await callback.message.edit_text('Выберите месяц', reply_markup=kb)


@dp.callback_query(F.data == 'days')
async def days_callback(callback: CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=even_days)
    await callback.message.edit_text('Выберите день', reply_markup=kb)


@dp.callback_query(F.data == 'hours')
async def hours_callback(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Введите текст напоминания.')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
