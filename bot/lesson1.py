from aiogram import Dispatcher, Bot, F
from aiogram import types
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = '8145770694:AAGbXWfsLTgvk3l51n7yvMibn-xdjDUGeyE'
dp = Dispatcher()

asosiy_menu = [
    [types.KeyboardButton(text='Kompaniya haqida'),
     types.KeyboardButton(text='Bizning mentorlar')],
    [types.KeyboardButton(text='Kurslarimiz')],
    [
        types.KeyboardButton(text='Kontaktlar'),
        types.KeyboardButton(text='Til')
    ]
]
asosiy = types.ReplyKeyboardMarkup(keyboard=asosiy_menu, resize_keyboard=True)

ichki_menu = [
    [
        types.KeyboardButton(text='Python'),
        types.KeyboardButton(text='Frontend')
    ],
    [
        types.KeyboardButton(text='Robototexnika'),
        types.KeyboardButton(text='Scratch')
    ],
    [
        types.KeyboardButton(text='Ortga')
    ]
]

ichki = types.ReplyKeyboardMarkup(keyboard=ichki_menu, resize_keyboard=True)

mentor_images = {"Bunyod Naimov": "https://framerusercontent.com/images/kXVV58GAu8fRErxTCCErYzk0i4.webp",
                 "Shohruh Abdurahmon": "https://framerusercontent.com/images/YqHAVasnW1eTKymnTB5dqiUMA.webp",
                 "Muhammadaziz To'lqinboyev": "https://framerusercontent.com/images/QzA0DHsPdTOxQ62dFyWslK4mT1Y.webp",
                 "Daler Badiyev": "https://framerusercontent.com/images/KNPILEJeDuGPQhkVMZY35hsyltg.webp",
                 "Asilbek Mamadaliyev": "https://framerusercontent.com/images/YxvMJWtMDSRGPD2IabC9CQdlBiU.webp",
                 "Habibulloh Nuriddin": "https://framerusercontent.com/images/rTCJHxT1yCe2LsYwsfZFrrBDds.webp",
                 "Asliddin Abdullayev": "https://framerusercontent.com/images/s6j0WzUvfog8RJHmnTeOurwR4.webp"}


# builder = InlineKeyboardBuilder()
# # 1 - Qator
# builder.row(
#     types.InlineKeyboardButton(text="1", callback_data="first_button"),
#     types.InlineKeyboardButton(text="2", callback_data="second_button")
# )
# # 2 - Qator
# builder.row(
#     types.InlineKeyboardButton(text="3", callback_data="third_button"),
#     types.InlineKeyboardButton(text="4", callback_data="fourth_button")
# )
#   

@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(f'Salom', reply_markup=asosiy)


@dp.message(F.text == 'Kompaniya haqida')
async def about_company(message: Message):
    await message.answer_photo(
        photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMx0I9OaWlz2o2nAPcy-72L9BrmD8telSDSQ&s',
        caption="8 yillik tajribaga, 2000 mingdan ortiq o'quvchilar va tarjibali mentorlar ega")


@dp.message(F.text == "Bizning mentorlar")
async def menu_handler(message: types.Message):
    for name, image in mentor_images.items():
        await message.answer_photo(photo=image,
                                   caption=f"Mentor: {name}")


@dp.message(F.text == 'Kurslarimiz')
async def hello(message: Message):
    await message.answer('python', reply_markup=ichki)


@dp.message(F.text == 'Ortga')
async def bye(message: Message):
    await message.answer('ortga', reply_markup=asosiy)


if __name__ == '__main__':
    bot = Bot(TOKEN)
    dp.run_polling(bot)
