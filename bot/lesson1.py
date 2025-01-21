from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = '8145770694:AAGbXWfsLTgvk3l51n7yvMibn-xdjDUGeyE'
dp = Dispatcher()


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
