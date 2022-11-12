from types import NoneType
from aiogram import types, Dispatcher
from create_bot import dp
import string, json
import datetime
import requests

from data_base.sqlite_db import get_id, sql_add_command, sql_read_id, sql_read_several
logs_num = 0
API_URL = 'https://7012.deeppavlov.ai/model'

#@dp.message_handler()
async def echo_send(message : types.Message):
    
    id_command = await get_id()
    if type(id_command[0]) != NoneType:
        id_command = id_command[0] + 1
    else:
        id_command = 1
    data = {'id': id_command,'time_id': datetime.datetime.now(), 'user_id':message.from_user.id, 'data': message.text}
    await sql_add_command(data)
    await sql_read_id(id_command)
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()} \
            .intersection(set(json.load(open('cenz.json')))):
            await message.reply('Mат запрещен!')
            await message.delete()
        
    if message.text.split()[0] == 'printlogs' and len(message.text.split()) == 2:
        if message.text.split()[1].isdigit():
            await sql_read_several(message)
    else:
        print('hello')
        print(f'Text = {message.text}')
        data = {'question_raw':  message.text}
        res = requests.post(API_URL, json=data, verify=False).json()
        print(res[0][0])
    

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)




   
