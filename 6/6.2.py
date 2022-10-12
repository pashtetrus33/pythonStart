# Задача 2.3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 2, 2: 4, 3: 7, 4: 9, 5: 12, 6: 14}

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
def sequence(number):
        return[((1 + 1 / n)**n) for n in range (1, number + 1)] 
def sequence_sum(number):
        return sum([((1 + 1 / n)**n) for n in range (1, number + 1)])
while True:
    number = inputInt('Программа выводит на экран сумму n чисел последовательности $(1+\\frac 1 n)^n$.\n\nВведите число n: ')
    #print(f'Последовательность для n = {number}: {sequence(number)}')
    list_sum = []
  
    # До code review

    # print(f'Для n = {number}: [', end='')
    # for i in range (1, number + 1):
    #     list_sum.append(round(sequence_sum(i)))
    #     if i != number:
    #         print(f'{i}: {list_sum[i-1]},', end=' ')
    #     else:
    #         print(f'{i}: {list_sum[i-1]}]', end=' ')
    
    # После code review
    print(f'Для n = {number}:',*[(i, round(sequence_sum(i))) for i in range(1, number + 1)])
   
    decision = input('\n\nДля продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
        break
