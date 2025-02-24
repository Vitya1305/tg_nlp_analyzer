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
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Жду текст...",
    selective=True
)
