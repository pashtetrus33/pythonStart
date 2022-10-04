# Задача 3.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import os
import random
from time import sleep

# метод очистки консоли
def clear(): return os.system('cls')

# метод проверки на ввод натурального числа
def input_natural(prompt=None):  
    while True:
        s = input(prompt)
        try:
            if int(s) > 0:
                return int(s)
            else:
                print('Ошибка. Ожидалось натуральное число.')
                sleep(2)
                clear()
        except ValueError:
            print('Ошибка. Ожидалось натуральное число.')
            sleep(2)
            clear()

def fill_numbers_list(length, filename):
    with open(filename,'w') as data:
        for i in range(length):
            value = random.randint(0,9)
            data.write(str(value)+ ' ')

def read_numbers_list(data_file):
    numbers_list = []
    with open(data_file,'r') as data:
        for line in data:
            numbers_list =line.split()
        return numbers_list           

while True:
    clear()
    #numbers_list = [1,2,6,8,0,55,3,5,77,4,1,2,5,6]    
    numbers_length = input_natural('Программа выведет список неповторяющихся элементов исходной последовательности\nВведите длину последовательности: ')
    fill_numbers_list(numbers_length, 'file_of_numbers.txt')
    numbers_list = read_numbers_list('file_of_numbers.txt')
    answer_list = []
    for i in numbers_list:
        if numbers_list.count(i) == 1:
            answer_list.append(i)

    print(f'Исходная последовательность (длина {numbers_length}): {numbers_list}')
    print(f'Cписок невовторяющихся элементов (длина {len(answer_list)}): {answer_list}')
    decision = input('Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
        break