from aiogram import Dispatcher, Bot
from aiogram import types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = '8145770694:AAGbXWfsLTgvk3l51n7yvMibn-xdjDUGeyE'
dp = Dispatcher()

builder = InlineKeyboardBuilder()
# 1 - Qator
builder.row(
    types.InlineKeyboardButton(text="1", callback_data="first_button"),
    types.InlineKeyboardButton(text="2", callback_data="second_button")
)
# 2 - Qator
builder.row(
    types.InlineKeyboardButton(text="3", callback_data="third_button"),
    types.InlineKeyboardButton(text="4", callback_data="fourth_button")
)


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('2+2')


if __name__ == '__main__':
    bot = Bot(TOKEN)
    dp.run_polling(bot)
