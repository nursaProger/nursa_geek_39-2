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
    random_profile_button = InlineKeyboardButton(
        "View Profiles 👍🏻👎🏻",
        callback_data="random_profile"
    )
    my_profile_button = InlineKeyboardButton(
        "Profile 🐲",
        callback_data="my_profile"
    )
    reference_menu_button = InlineKeyboardButton(
        "Reference Menu 💵",
        callback_data="reference_menu"
    )
    check_ban_button = InlineKeyboardButton(
        "Check Ban Status",
        callback_data="check_ban"
    )

    markup.add(registration_button)
    markup.add(questionnaire_button)
    markup.add(random_profile_button)
    markup.add(my_profile_button)
    markup.add(reference_menu_button)
    markup.add(check_ban_button)
    return markup








