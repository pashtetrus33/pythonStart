# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

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
            sleep(2)
            clear()
while True:
    number = inputInt('Программа принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.\n\nВведите число: ')
    
    if number % 30 != 0 and number % 5 == 0 and (number % 10 == 0 or number % 15 == 0):
        print(f'Число {number} -> условие выполнено')
    else:
        print(f'Число {number} -> условие не выполнено')
    print()
    decision = input('Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') | (decision.lower() == 'у'):
        break