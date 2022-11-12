from aiogram.utils import executor
from create_bot import dp
from handlers import bot_commands, other
from data_base import sqlite_db

async def on_startup(_):
    print('Bot is online')
    sqlite_db.sql_start()

bot_commands.register_handlers_calc(dp)

other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)