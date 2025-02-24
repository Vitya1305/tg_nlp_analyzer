import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from telegram_bot import keyboards
from model_training import ai

TOKEN = "7858597411:AAFtGw0O3KLLLptoFs3yxgJ7a019iASgaDA"

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
    await  msg.answer("Привет! Я бот для распознавания настроений сообщений.", reply_markup=keyboards.main)

@dp.message()
async def allQuest(msg: types.Message):
    input_text = msg.text
    anal = ai.analyse(input_text)
    await msg.answer(anal)
    print(anal, input_text)


if __name__ == '__main__':
    ai.init('2')
    asyncio.run(main())