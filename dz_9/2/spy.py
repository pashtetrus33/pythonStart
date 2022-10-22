import datetime
from telegram import Update
from telegram.ext import ContextTypes




async def log(update: Update, context):
    file = open('data.csv', 'a', encoding='utf-8')
    file.write(f'{datetime.datetime.now()},{update.effective_user.first_name},{update.effective_user.id},{update.message.text}\n')
    file.close()
