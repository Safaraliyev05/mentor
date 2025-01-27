from aiogram import Dispatcher, Bot, F
from aiogram import types
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = '8145770694:AAGbXWfsLTgvk3l51n7yvMibn-xdjDUGeyE'
dp = Dispatcher()

asosiy_menu = [
    [types.KeyboardButton(text='python'),
     types.KeyboardButton(text='frontend')]
]
asosiy = types.ReplyKeyboardMarkup(keyboard=asosiy_menu, resize_keyboard=True)

python_button = [
    [types.KeyboardButton(text='ortga')]
]
python = types.ReplyKeyboardMarkup(keyboard=python_button, resize_keyboard=True)


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


@dp.message(F.text == 'python')
async def hello(message: Message):
    await message.answer('python', reply_markup=python)


@dp.message(F.text == 'ortga')
async def bye(message: Message):
    await message.answer('ortga', reply_markup=asosiy)


if __name__ == '__main__':
    bot = Bot(TOKEN)
    dp.run_polling(bot)
