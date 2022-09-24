# Задача 4: Программа принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример
# - А (3,6); B (2,1) -> 5,09
# - А (7,-5); B (1,-1) -> 7,21

import math
import os
from time import sleep
clear = lambda: os.system('cls')
clear()  # очистка консоли
def inputInt(prompt=None):  # метод проверки на ввод целого числа
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print('Ошибка. Ожидалось целое число')
            sleep(1)
            clear()                       
while True:
    print('Программа принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.\n')
    xA = inputInt('Вводим точку А. Введите X = ')
    yA = inputInt('Вводим точку А. Введите Y = ')
    xB = inputInt('Вводим точку B. Введите X = ')
    yB = inputInt('Вводим точку B. Введите Y = ')
    distance =  math.sqrt((xB - xA)**2 + (yB - yA)**2) 
    print(f'\n-A ({xA},{yA}); B ({xB},{yB}) -> {math.floor(distance*100)/100}\n')
    decision = input('Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') | (decision.lower() == 'у'):
        break