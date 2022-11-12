import os
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import requests


storage=MemoryStorage()
bot  = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)


def rational():
    data = {'x': 'Сколько сейчас времени?'}
    res = requests.post('https://7012.deeppavlov.ai/model', json=data).json()

    print(res[0][0])
    print(res)
   
rational()