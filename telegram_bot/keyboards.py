from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='О боте'),
        KeyboardButton(text='Выбрать модель')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Жду текст...",
    selective=True
)
def generate_inlineKeyboard(models):
    result_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=model, callback_data=model)]
                                                            for model in models])
    return result_keyboard