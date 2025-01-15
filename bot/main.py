import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from utils import get_weather_data

TOKEN = '7356873796:AAHOeoPwMkFKL6lEvVYH_qv92y7CZEsnvzA'
dp = Dispatcher()


@dp.message(CommandStart)
async def start(message: Message):
    await message.answer('Welcome to weather bot')


@dp.message(Command('weather'))
async def weather(message: Message):
    city = message.text
    result = get_weather_data(city)
    temp = str(result['main']['temp']) + '°C'
    await message.answer(temp)


async def main():
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
