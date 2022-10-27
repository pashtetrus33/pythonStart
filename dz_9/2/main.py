from bot_commands import *
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters



app = ApplicationBuilder().token('TOKEN').build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("csum", csum_command))
app.add_handler(CommandHandler("guess", guess))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print('Server is running')
app.run_polling()