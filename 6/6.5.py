# Задача 3.2.Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
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
    size = inputInt('Программа находит найдёт произведение пар чисел списка.\nВведите количество чисел в списке: ')
    min = inputInt('Введите минимальное значение элементов в списке: ')
    max = inputInt('Введите максимальное значение элементов в списке: ')
    if min > max:
        min,max = max,min

    # Before code review
    # for i in range (size):
    #     list_numbers.append(random.randint(min, max))
    
    # After code review
    list_numbers = [random.randint(min, max) for i in range(size)]
    print(f'Cгенерированный список: {list_numbers}')

    # Решение с zip:
    list_1 = [list_numbers[x] for x in range(len(list_numbers)//2)]
    list_2 = [list_numbers[x] for x in range(len(list_numbers)) if x > len(list_numbers)//2]
    list_2.reverse()
    print(list_1)
    print(list_2)
    print(list(zip(list_1,list_2)))
    
    #print(list(zip(list_numbers,)))

    # Before code review
    # for i in range(len(list_numbers)//2):
    #     multiplies.append(list_numbers[i]*list_numbers[-i-1])
    
    # After code review
    multiplies =[list_numbers[i]*list_numbers[-i-1] for i in range(len(list_numbers)//2)]
    
    
    if (len(list_numbers) % 2 !=0):
        multiplies.append(list_numbers[len(list_numbers)//2]**2)
        
    print(f'{list_numbers} -> {multiplies}')
    decision = input(
        'Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
        break