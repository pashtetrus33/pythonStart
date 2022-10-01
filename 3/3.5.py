# Задача 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

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
def fib(number):
    if number in [1,2]:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)

def negofib(number):
    if number in [-2, -1]:
        return (-1)**(number +1)
    else:
        return negofib(number + 2) - negofib(number + 1)

while True:
    number = inputInt('Программа выводит список чисел Фибоначчи, в том числе для отрицательных индексов.\n\nВведите число n: ')
    fib_list = []
    if number > 0:
        for i in range(1,number+1):
            fib_list.append(fib(i))
        print(f'Последовательность Фибона́ччи для n = {number}: {fib_list}')
    elif number < 0:
        for i in range(-1,number-1, -1):
                fib_list.append(int(negofib(i)))
        print(f'Последовательность негафибоначчи для n = {number}: {fib_list}')
    else:
        print(f'Последовательность Фибона́ччи для n = 0: [0]')


    decision = input('\n\nДля продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
        break
