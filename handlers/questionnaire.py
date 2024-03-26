from aiogram import types, Dispatcher
from config import bot
from keyboards import questionnaire_inline_buttons
from database.bot_db import Database


questions = {
    'Toyota or Honda': ['Toyota', 'Honda'],
    'Samsung or Iphone': ['Samsung', 'Iphone'],
    'Minecraft or Terraria':['Minecraft', 'Terrariaa']
}
async def start_questionnaire_call(call: types.CallbackQuery):
    for question, options in questions.items():
        await bot.send_message(
            chat_id=call.from_user.id,
            text=question,
            reply_markup=await questionnaire_inline_buttons.start_questionnaire_keyboard(options)
        )
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Toyota or Honda?",
        reply_markup=await questionnaire_inline_buttons.start_questionnaire_keyboard()
    )

    await bot.send_message(
        chat_id=call.from_user.id,
        text="Samsung or Honda?",
        reply_markup=await questionnaire_inline_buttons.start_questionnaire_keyboard()
    )

    await bot.send_message(
        chat_id=call.from_user.id,
        text="Minecraft or Terraria",
        reply_markup=await questionnaire_inline_buttons.start_questionnaire_keyboard()
    )



async def toyota_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Toyota is a good car",
    )

async def honda_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Honda is a good car",
    )



async def samsung_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Samsung is a good phone",
    )


async def iphone_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Iphone is a good phone",
    )


async def minecraft_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Minecraft is a good game",
    )

async def terraria_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="terraria is a good game",
    )


async def check_ban_status(call: types.CallbackQuery):
    db = Database()
    banned_count = db.sql_check_banned_user(call.from_user.id)
    if banned_count > 0:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"You have been banned with {banned_count} violations"
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="You are not banned"
        )



def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        check_ban_status,
        lambda call: call.data == "check_ban"
    )

    dp.register_callback_query_handler(
        start_questionnaire_call,
        lambda call: call.data == "start_questionnaire"
    )
    dp.register_callback_query_handler(
        toyota_call,
        lambda call: call.data == "toyota"
    )
    dp.register_callback_query_handler(
        honda_call,
        lambda call: call.data == "honda"
    )
    dp.register_callback_query_handler(
        samsung_call,
        lambda call: call.data == "samsung"
    )
    dp.register_callback_query_handler(
        iphone_call,
        lambda call: call.data == "iphone"
    )
    dp.register_callback_query_handler(
        minecraft_call,
        lambda call: call.data == "minecraft"
    )
    dp.register_callback_query_handler(
        terraria_call,
        lambda call: call.data == "terraria"
    )