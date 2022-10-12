# Задача 2.2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial
import os
from time import sleep
def clear(): return os.system('cls')

clear()  # очистка консоли

def inputInt(prompt=None):  # метод проверки на ввод целого числа
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print('Ошибка. Ожидалось целое число.')
            sleep(2)
            clear()

while True:
    number = inputInt('Программа принимает на вход число N и выдает набор произведений чисел от 1 до N.\n\nВведите число: ')
    result = []
    # До code review
    
    # mult = 1
    # for i in range(1, number + 1):
    #     mult *= i
    #     result.append(mult)
    
    # После  code review
    f = lambda x: 1 if x == 0 else x * factorial(x - 1)
    result =  list(f(i) for i in range(1, number +1))
    
    print(f'Набор поризведений числа {number} = {result}')
    decision = input(
        'Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
        break