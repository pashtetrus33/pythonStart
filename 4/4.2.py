# Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import os
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
def is_number_simple (number):
    count =0
    if number > 1:
        for i in range(2, number+1):
            if number % i == 0:
                count += 1
        return count == 1
    else:
        return False       
while True:
    clear()
    number = input_natural('Программа выводит список простых множителей натурального числа N.\nВведите натуральное число: ')
    simple_list = []
    answer_list = []
    for i in range(2, number + 1):
        if is_number_simple(i):
            simple_list.append(i)
    if number > 1:
        if not is_number_simple(number):
            # Для вывода списка уникальных простых множителей
            # for i in simple_list:
            #     if number % i == 0:
            #         answer_list.append(i)
            # print(f'Список простых чисел от 2 до {number}: {simple_list}')
            i = 0
            # Для вывода списка простых множителей составляющих число number
            number_original = number
            while number > 1:
                    if number % simple_list[i] == 0:
                        answer_list.append(simple_list[i])
                        number //= simple_list[i]
                    else:
                        i += 1
            print(f'Список простых чисел от 2 до {number_original}: {simple_list}')
        else:
            answer_list.append(number)
    else:
        print('Число 1 не имеет простых делителей и не является ни простым, ни составным числом.')
        sleep(2)
        clear()
        continue
    print(f'Ответ: {answer_list}')
    decision = input('Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
        break