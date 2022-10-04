# Задача 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import os
import math
from time import sleep
def clear(): return os.system('cls')
def input_int(prompt=None):  # метод проверки на ввод вещественного числа
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print('Ошибка. Ожидалось целое число.')
            sleep(2)
            clear()

while True:
    clear()  # очистка консоли
    d = input_int('Программа выводит число π с заданной точностью.\nВведите количество знаков после запятой: ')
    if 1 <= d <= 10:
        pi = (math.pi*10**d//1)/10**d
        print(f'При d = {1/10**d}  π = {pi}')
    else:
        print(f'Вы ввели точность: {d} неверно (1 <= d <= 10)')
        sleep(2)
        continue
    decision = input('Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
        break