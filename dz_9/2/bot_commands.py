import datetime
from telegram import Update
from telegram.ext import ContextTypes
from spy import *
from random import randint

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'Здравствуйте!\nЯ бот Павла Баканова. Команда /help выведет все мои возможности!')

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum\nComplex sum:/csum\nGame:/guess')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    items = msg.split()
    if len(items) == 3:
        try:
            x = int(items[1])
            y = int(items[2])
            await update.message.reply_text(f'{x}+{y}={x+y}')
        except:
            await update.message.reply_text(f'I need 2 digits')
    else:
        await update.message.reply_text(f'We need 2 digits')

async def csum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    items = msg.split()
    if len(items) == 5:
        try:
            x = int(items[1])
            x_im = int(items[2])
            y = int(items[3])
            y_im = int(items[4])
            num1 = complex(x,x_im)
            num2 = complex(y,y_im)
            csum = num1 + num2
            await update.message.reply_text(f'{num1}+{num2}={csum}')
        except:
            await update.message.reply_text(f'I need 4 digits')
    else:
        await update.message.reply_text(f'We need 4 digits')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)
    
async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Guess digit from 1 to 10')
    await log(update, context)
    chislo_comp = randint(1, 10) 
    msg = update.message.text
    items = msg.split()
    if len(items) == 2:
        try:
            x = int(items[1])
            await update.message.reply_text(chislo_comp)
            if x == chislo_comp:
                await update.message.reply_text(f'You won!')
            else:
                await update.message.reply_text(f'You lose!')
        except:
            await update.message.reply_text(f'I need 1 digit')      
    else:
        await update.message.reply_text(f'I need 1 argement')