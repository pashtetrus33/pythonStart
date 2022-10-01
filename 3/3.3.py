# Задача 3.Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math
import os
import random
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
while True:
    clear()  # очистка консоли
    size = inputInt('Программа находит разницу между максимальным и минимальным значением дробной части элементов..\nВведите количество чисел в списке: ')
    min_value = inputInt('Введите минимальное целое значение элементов в списке: ')
    max_value = inputInt('Введите максимальное целое значение элементов в списке: ')
    if min_value > max_value:
        print('Min больше Max, мы поменяли их местами.')
        min_value,max_value = max_value,min_value
    if min_value == max_value:
        print('Ошибка ввода. Min равен Max, повторите ввод.')
        sleep(2)
        continue
    list_numbers = []
    for i in range (size):
        list_numbers.append(round(random.randint(min_value, max_value-1) + random.random(),2))
    print(f'Cгенерированный список: {list_numbers}')
    list_floats =[]
    for i in list_numbers:
        list_floats.append(round(i - int(i),3))
        #list_floats.append(round(100*(i - int(i))))
    index_max = list_floats.index(max(list_floats))
    index_min = list_floats.index(min(list_floats))
    print(f'Cписок дробных частей:  {list_floats}') 
    print(f'Наибольшая дробная часть: {max(list_floats)} c индексом: {index_max}') 
    print(f'Наименьшая дробная часть: {min(list_floats)} c индексом: {index_min}')
    max_float = list_floats[index_max]
    min_float = list_floats[index_min]
    print(f'Разница между максимальным и минимальным значением дробной части элементов списка {list_numbers} -> {round((max_float - min_float),3)}')
    decision = input(
        'Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
        break