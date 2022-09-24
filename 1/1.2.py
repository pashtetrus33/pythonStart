# Задача 2: Программа принимает на вход координаты точки (X и Y) причем X != 0 и Y !=0 и выдает номер четверти плоскости, в которой находтися эта точка (или на кокой оси она находится).
# Пример
# - x=34; y=-30 -> 4
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
            print('Ошибка. Ожидалось целое число (не равное 0)')
            sleep(1)
            clear()                     
while True:
    x = 0
    while (x == 0):
        clear()
        x = inputInt('Программа принимает на вход координаты точки (X и Y) причем X != 0 и Y !=0 и выдает номер четверти плоскости, в которой находтися эта точка (или на кокой оси она находится).\n\nВведите координату X (!=0): ')
        continue   
    y = 0
    while (y == 0):
        y = inputInt('Введите координату Y (!=0): ')
        continue
    print()
    if (x > 0) and (y > 0):
        print(f'- x={x}; y={y} -> 1') 
    elif (x < 0) and (y > 0):
        print(f'- x={x}; y={y} -> 2')
    elif (x < 0) and (y < 0):
        print(f'- x={x}; y={y} -> 3')
    else:
        print(f'- x={x}; y={y} -> 4')
    decision = input('\nДля продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') | (decision.lower() == 'у'):
        break