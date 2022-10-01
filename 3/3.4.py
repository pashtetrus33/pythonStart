# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
import os
import random
import re
from time import sleep
def clear(): return os.system('cls')
def inputInt(prompt=None):  # метод проверки на ввод вещественного числа
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print('Ошибка. Ожидалось целое число.')
            sleep(2)
            clear()
# Метод подсчета разрядности числа в двоичной системе счисления
def Length_number_count(number):
    binary_length = 0
    while number > 0:
        number //= 2
        binary_length += 1
    return binary_length

#метод перевода чилса из десятичной в двоичную систему счисления
def Decimal_binary(number, length):
    if number == 0:
        print(f'Число 0 в двоичной системе счисления равно 0')
    elif number < 0:
        print('Программа не работает с отрицательными числами!') 
    else:
        result = ''
        original_number = number
        while number > 0:
            result += str(number % 2)
            number //= 2
        result = result[::-1]
        print(f'Число {original_number} в двоичной системе счисления равно {result}')
    
while True:
    clear()  # очистка консоли
    num_decimal = inputInt('Программа преобразовывает десятичное число в двоичное.\nВведите целое число: ')
    length = Length_number_count(num_decimal)
    Decimal_binary(num_decimal, length)
    decision = input(
        'Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
        break