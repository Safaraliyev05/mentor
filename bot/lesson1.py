from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = '7356873796:AAHOeoPwMkFKL6lEvVYH_qv92y7CZEsnvzA'
dp = Dispatcher()


@dp.message(CommandStart)
async def start(message: Message):
    await message.answer('Welcome to bot')


if __name__ == '__main__':
    bot = Bot(TOKEN)
    dp.run_polling(bot)
