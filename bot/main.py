import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from keyboards import key, category, electronics, home_elect, clothes, shoes, accessories, health, hobby, sport, avto, \
    builder

TOKEN = "6436075723:AAEDRQxRGW4qs2hP5DfKR6sxjG5W2UjSmpA"

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Assalomu aleykum {message.from_user.first_name} aka")


# @dp.message(Command('image'))
# async def image(message: Message):
#     p1 = 'https://images.app.goo.gl/EqdxRVYd9FzMoMY58'
#     p2 = 'https://images.app.goo.gl/Cg6zUmwBTdT23xXF6'
#     p3 = 'https://images.app.goo.gl/jZNkYSQEHhbFYUYy5'
#     p4 = 'https://images.app.goo.gl/hiatfaLKagNxD8iq5'
#     p5 = 'https://images.app.goo.gl/oTrqqbc29DARamqp7'
#
#     lst = [p1, p2, p3, p4, p5]
#     result = random.choice(lst)
#     await message.answer_photo(photo=result, caption='🐒 Shimpanze == 👦 Diyor')


@dp.message(Command('button'))
async def button_start(message: Message):
    await message.answer('tanla', reply_markup=key)


@dp.message(Command('shop'))
async def shop(message: Message):
    await message.answer('Category tanlang', reply_markup=category)

    @dp.message(F.text == 'Elektronika')
    async def technology(message: Message):
        await message.answer('Eletronika tanlang', reply_markup=electronics)

        @dp.message(F.text == 'Ortga')
        async def back(message: Message):
            await message.answer('Ortga', reply_markup=category)

    @dp.message(F.text == 'Maishiy Texnika')
    async def technology(message: Message):
        await message.answer('Modelni tanlang', reply_markup=home_elect)

        @dp.message(F.text == 'Ortga')
        async def back(message: Message):
            await message.answer('Modelni tanlang', reply_markup=category)

    @dp.message(F.text == 'Kiyim')
    async def technology(message: Message):
        await message.answer('Modelni tanlang', reply_markup=clothes)

        @dp.message(F.text == 'Ortga')
        async def back(message: Message):
            await message.answer('Modelni tanlang', reply_markup=category)

        # inline button
        @dp.message(F.text == 'Erkakalar kiyimi')
        async def e(message: Message):
            await message.answer_photo(photo='https://images.uzum.uz/cl470gl6sfhgee0kod40/original.jpg',
                                       caption='Spartivka', reply_markup=builder.as_markup())

    @dp.message(F.text == 'Poyabzallar')
    async def technology(message: Message):
        await message.answer('Modelni tanlang', reply_markup=shoes)

        @dp.message(F.text == 'Ortga')
        async def back(message: Message):
            await message.answer('Modelni tanlang', reply_markup=category)

    @dp.message(F.text == 'Aksessuarlar')
    async def technology(message: Message):
        await message.answer('Modelni tanlang', reply_markup=accessories)

        @dp.message(F.text == 'Ortga')
        async def back(message: Message):
            await message.answer('Modelni tanlang', reply_markup=category)

    @dp.message(F.text == 'Salomatlik')
    async def technology(message: Message):
        await message.answer('Modelni tanlang', reply_markup=health)

        @dp.message(F.text == 'Ortga')
        async def back(message: Message):
            await message.answer('Modelni tanlang', reply_markup=category)

    @dp.message(F.text == 'Xobbi')
    async def technology(message: Message):
        await message.answer('Modelni tanlang', reply_markup=hobby)

        @dp.message(F.text == 'Ortga')
        async def back(message: Message):
            await message.answer('Modelni tanlang', reply_markup=category)

    @dp.message(F.text == 'Sport')
    async def technology(message: Message):
        await message.answer('Modelni tanlang', reply_markup=sport)

        @dp.message(F.text == 'Ortga')
        async def back(message: Message):
            await message.answer('Modelni tanlang', reply_markup=category)

    @dp.message(F.text == 'Avtotovarlar')
    async def technology(message: Message):
        await message.answer('Modelni tanlang', reply_markup=avto)

        @dp.message(F.text == 'Ortga')
        async def back(message: Message):
            await message.answer('Modelni tanlang', reply_markup=category)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())