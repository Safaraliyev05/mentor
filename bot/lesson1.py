from aiogram import Dispatcher, Bot
from aiogram import types
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = '8145770694:AAGbXWfsLTgvk3l51n7yvMibn-xdjDUGeyE'
dp = Dispatcher()

buttons = [
    [types.KeyboardButton(text='1'),
     types.KeyboardButton(text='2')],

    [types.KeyboardButton(text='3'),
     types.KeyboardButton(text='4')],
]
reply_contact = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


@dp.message(Command('button'))
async def button_start(message: Message):
    await message.answer('Ikki qator tugmalar', reply_markup=reply_contact)


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
