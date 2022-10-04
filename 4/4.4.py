# Задача 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

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
def random_number(min, max):
    return random.randint(min,max)
def append_polynomial_to_file(polinomial, filename):
    with open(filename,'a') as data:
        data.write(polinomial) 
def fill_coefficients(k):
    coefficients = []
    for i in range(k+1):
        value = random_number(0,100)
        if value == 0 and k == 1 and i == 0:
           value = 1
        coefficients.append(value)
    count =0
    for i in coefficients:
        if i == 0:
            count += 1
    if count == len(coefficients):
        coefficients[-1] = 1
    return coefficients
def create_polynomial(coefficients):
    answer = ''
    for i in range(k, -1, -1):
        if i == 0:
            add_part = str(coefficients[k-i]) + ' = 0\n'
        elif coefficients[k-i] == 1 and i != 1:
            add_part = 'x^' + str(i) + ' + '
        elif coefficients[k-i] == 1 and i == 1:
            add_part = 'x + '
        elif i == 1 and coefficients[k-i] != 0:
            add_part = str(coefficients[k-i]) + '*' + 'x + '
        elif coefficients[k-i] == 0:
            add_part = ''
        else:
         add_part = str(coefficients[k-i])+ '*' + 'x^' + str(i) + ' + '
        answer += add_part
    answer = answer.replace('+ 0 = 0','= 0')
    return answer 

while True:
    clear()    
    k = input_natural('Программа формирует случайным образом список коэффициентов (значения от 0 до 100)\
 многочлена и записывает в файл многочлен степени k.\nВведите степень к: ')
    coefficients = fill_coefficients(k)
    answer = create_polynomial(coefficients)
    append_polynomial_to_file(answer,'file_with_polynomials2.txt')
    
    decision = input('Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
        break
