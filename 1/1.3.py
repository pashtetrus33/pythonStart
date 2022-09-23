# Задача 3: Программа по заданному номеру четверти показывает диапазон возможных координат точек в этой четверти (x и y).

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
            print('Ошибка. Ожидалось целое число в диапазоне 1-4')
            sleep(1)
            clear()                       
while True:
    quarter = 0
    while (quarter > 4) | (quarter < 1):
        clear()
        quarter = inputInt('Программа по заданному номеру четверти показывает диапазон возможных координат точек в этой четверти (x и y).\n\nВведите номер четверти (1-4): ')
        continue
    print()
    if (quarter == 1):
        print(f'- x > 0; y > 0') 
    elif (quarter == 2):
        print(f'- x < 0; y > 0') 
    elif (quarter == 3):
        print(f'- x < 0; y < 0')
    else:
        print(f'- x > 0; y < 0')
    decision = input('\nДля продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if ((decision.lower() == 'e') | (decision.lower() == 'у')):
        break