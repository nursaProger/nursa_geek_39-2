from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Questionnaire",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Registration",
        callback_data="registration"
    )
    check_ban_button = InlineKeyboardButton(
        "Check Ban Status",
        callback_data="check_ban"
    )

    markup.add(registration_button)
    markup.add(questionnaire_button)
    markup.add(check_ban_button)
    return markup








