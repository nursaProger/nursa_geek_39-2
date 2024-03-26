from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from database import bot_db
from keyboards import start_menu
import const



async def start_button(message: types.Message):
    print(message)

    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'Hello {message.from_user.first_name}'
    )

async def start_button(message: types.Message):
    print(message)
    db = bot_db.Database()
    db.sql_insert_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )



    # with open(MEDIA_DESTINATION + "bot-pic.png", 'rb') as photo:
    #     await bot.send_photo(
    #         chat_id=message.from_user.id,
    #         photo=photo,
    #         caption=const.START_MENU_TEXT.format(
    #             user=message.from_user.first_name
    #         ),
    #         reply_markup=await start_inline_buttons.start_keyboard()
    #     )



    with open(MEDIA_DESTINATION + "ani_bot.gif", 'rb') as ani:
        await bot.send_animation(
            chat_id=message.from_user.id,
            animation=ani,
            caption=const.START_MENU_TEXT.format(
                user=message.from_user.first_name
            ),
            reply_markup=await start_menu.start_keyboard()
        )




def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_button,
        commands=['start']
    )
