import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart
from telegram_bot import keyboards
from model_training import ai

TOKEN = "7858597411:AAFtGw0O3KLLLptoFs3yxgJ7a019iASgaDA" # токен бота телеграм
ai.model_names = ['tz', 'another model']    # tz - модель обученная на датасете данном по тз; another model - модель обученная на расширенном датасете https://www.kaggle.com/datasets/simaanjali/emotion-analysis-based-on-text
default_model = 'tz'
start_text = 'Привет! Этот бот создан для определения настроения текста!'
text_info = 'Для того чтобы определить настроение просто отправь мне текст 😉\nТак же у вас есть возможность выбрать модель: /choose либо кнопке "Выбрать модель"\nПолучить вновь эту подсказку: /info либо кнопкой "О боте"'

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    #await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

@dp.startup()
async def on_startup():
    print('Done!')

@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer_sticker('CAACAgIAAxkBAANzZhJ4OrrcU5f5LOYlC7Huqac6Pg4AAtgPAAJI8mBLFfvE2nh0a5g0BA')
    await msg.answer(start_text, reply_markup=keyboards.main)
    await msg.answer(text_info)

@dp.message(Command('choose'))
async def choose_model_command(msg: types.Message):
    await msg.answer("Выберете модель", reply_markup=keyboards.generate_inlineKeyboard(ai.model_names))

@dp.message(Command('info'))
async def info_command(msg: types.Message):
    print(await bot.get_my_commands())
    await msg.answer(text_info)

@dp.message(F.text == 'Выбрать модель')
async def choose_model(msg: types.Message):
    await msg.answer("Выберете модель", reply_markup=keyboards.generate_inlineKeyboard(ai.model_names))

@dp.message(F.text == 'О боте')
async def info(msg: types.Message):
    await msg.answer(text_info)

@dp.callback_query(F.data.in_(ai.model_names))
async def callbacks_on_select_theme(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Модель успешно выбрана "{callback.data}"' if ai.init(callback.data) else 'Error :<')


@dp.message()
async def allQuest(msg: types.Message):
    input_text = msg.text
    anal = ai.analyse(input_text)

    await msg.answer(anal)
    print(anal, input_text)


if __name__ == '__main__':
    ai.init(default_model)
    asyncio.run(main())