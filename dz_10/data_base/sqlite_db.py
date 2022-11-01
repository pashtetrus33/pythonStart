from email import message
import sqlite3 as sq
from aiogram import types

def sql_start():  
    global base, cur
    base = sq.connect('log_calc.db')
    cur = base.cursor()
    if base:
        print('\nDB SQLITE3 is connected!\n')
    base.execute('CREATE TABLE IF NOT EXISTS log(id INT PRIMARY KEY, time_id DATE, user_id TEXT, data TEXT)')
    base.commit()

async def sql_add_command(data):
    cur.execute('INSERT INTO log VALUES(?,?,?,?)', tuple(data.values()))
    base.commit()

async def get_id():
    return cur.execute('SELECT MAX(id) FROM log').fetchone()
       
async def sql_read_id(id_com):
    for i in cur.execute('SELECT * FROM log WHERE id =?', (id_com,)).fetchall():
        print(f'{i[0]} Time: {i[1]} User_id: {i[2]} Data {i[3]}')

async def sql_read(message : types.Message):
    for i in cur.execute('SELECT * FROM log').fetchall():
        print(f'{i[0]} Time: {i[1]} User_id: {i[2]} Data {i[3]}')

async def sql_read_several(message : types.Message):
    for i in cur.execute(f'SELECT * FROM log ORDER BY id DESC LIMIT {message.text.split()[1]}').fetchall():
        print(f'{i[0]} Time: {i[1]} User_id: {i[2]} Data {i[3]}')
        await message.answer(f'{i[0]} Time: {i[1]} User_id: {i[2]} Data {i[3]}')
        

async def sql_read_to_bot(message : types.Message):
    for i in cur.execute('SELECT * FROM log').fetchall():
        await message.answer(f'{i[0]} Time: {i[1]} User_id: {i[2]} Data {i[3]}')



