# Задача 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
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
    size = inputInt('Программа находит сумму элементов списка, стоящих на нечётной позиции.\nВведите количество чисел в списке: ')
    min = inputInt('Введите минимальное значение элементов в списке: ')
    max = inputInt('Введите максимальное значение элементов в списке: ')
    if min > max:
        min,max = max,min
    list_numbers = []
    odd_elements =[]
    for i in range (size):
        list_numbers.append(random.randint(min, max))
    print(f'Cгенерированный список: {list_numbers}')
    summa = 0
    for i in range(1, len(list_numbers),2):
        odd_elements.append(list_numbers[i])
        summa += list_numbers[i]
    print(f'На нечетных позициях элементы {odd_elements}, ответ: {summa}')
    decision = input(
        'Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
        break