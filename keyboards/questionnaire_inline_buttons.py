from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)




async def start_questionnaire_keyboard(options):
    markup = InlineKeyboardMarkup()
    for option in options:
        button = InlineKeyboardButton(option, callback_data=option.lower())
        markup.add(button)
    return markup


