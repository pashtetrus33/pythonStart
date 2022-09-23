# Задача 1: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# 6 -> да
# 7 -> да
# 1 -> нет
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
            print('Ошибка. Ожидалось целое число от 1 до 7.')
            sleep(2)
            clear()
while True:
    number = inputInt('Программа принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.\n\nВведите целое число от 1 до 7: ')
    if ((number < 1) | (number > 7)):
        print('Ошибка. Ожидалось целое число от 1 до 7.')
        sleep(2)
        clear()
        continue 
    if ((number != 6) & (number != 7)):
        print(f'- {number} -> нет') 
    else:
        print(f'- {number} -> да')
    print()
    decision = input('Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if ((decision.lower() == 'e') | (decision.lower() == 'у')):
        break