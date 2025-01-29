from aiogram import Dispatcher, Bot
from aiogram import types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = '8145770694:AAGbXWfsLTgvk3l51n7yvMibn-xdjDUGeyE'
dp = Dispatcher()

# buttons = [
#     [types.KeyboardButton(text='1'),
#      types.KeyboardButton(text='2')],
#
#     [types.KeyboardButton(text='3'),
#      types.KeyboardButton(text='4')],
# ]
# reply_contact = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

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


@dp.message(Command('button'))
async def button_start(message: Message):
    await message.answer('Tugmalar', reply_markup=builder.as_markup())


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(f'Assalomu alaykum {message.from_user.first_name}')


@dp.message(Command("info"))
async def info(message: Message):
    await message.answer('info')


@dp.message(Command('picture'))
async def picture(message: Message):
    await message.answer_photo(
        photo='https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg',
        caption='Tree'
    )


if __name__ == '__main__':
    bot = Bot(TOKEN)
    dp.run_polling(bot)
