from string import digits
from types import NoneType
from typing import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp , bot
from aiogram.dispatcher.filters import Text
from data_base.sqlite_db import get_id, sql_add_command, sql_read, sql_read_id, sql_read_several, sql_read_to_bot
from keyboards import kb_calc
import datetime

calc_list = []
data = {}
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, f'Привет {message.from_user.full_name}! Я БОТ-КАЛЬКУЛЯТОР\nВведите выражение для раcчета: ', reply_markup=kb_calc)
        await bot.send_message(1293578282,f'@{message.from_user.username}')

        print ('\n',message.from_user.full_name,'\n')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите му:\nhttps://t.me/PythonPashtetBot')
        await bot.send_message(1293578282,f'@{message.from_user.username}')
        

async def enter_digit(message : types.Message):
    id_command = await get_id()
    if type(id_command[0]) != NoneType:
        id_command = id_command[0] + 1
    else:
        id_command = 1
    data = {'id': id_command,'time_id': datetime.datetime.now(), 'user_id':message.from_user.id, 'data': message.text}
    await sql_add_command(data)
    await sql_read_id(id_command)
    if message.text == 'Pow':
        message.text = '**'
    if message.text != "=":
        calc_list.append(message.text) 
    else:
        expression = " ".join(calc_list)
        result = "".join(calc_list)
        try:
            await message.answer(f'Результат:  {expression} = {round(eval(result),3)}')
            id_command += 1
            data2 = {'id': id_command,'time_id': datetime.datetime.now(), 'user_id':message.from_user.id, 'data': round(eval(result),3)}
            await sql_add_command(data2)
            await sql_read_id(id_command)
        except:
            await message.answer('Error in expression')
            id_command += 1
            data3 = {'id': id_command,'time_id': datetime.datetime.now(), 'user_id':message.from_user.id, 'data': 'Error in expression'}
            await sql_add_command(data3)
            await sql_read_id(id_command)
        calc_list.clear()
        
async def command_print_log_to_bot(message : types.Message):
    await message.answer('Bot Log:')
    await sql_read_to_bot(message)

async def command_print_log(message : types.Message):
    print('\nBot Log to Console:\n')
    await sql_read(message)

async def command_print_log_10(message : types.Message):
    print('\nBot Log to Console:\n')
    await sql_read_several(message)

def register_handlers_calc(dp : Dispatcher):
    
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(enter_digit,Text(equals=['0','1','2','3','4','5','6','7','8','9']))
    dp.register_message_handler(enter_digit,Text(equals=['+','-','*','Pow','/','//','%','(',')','.','=']))
    dp.register_message_handler(command_print_log_to_bot, commands=['printlog'])
    dp.register_message_handler(command_print_log_10, commands=['printlog10'])
    dp.register_message_handler(command_print_log, commands=['console'])