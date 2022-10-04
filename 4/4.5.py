# Задача 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import os
import random
import re
from time import sleep
# метод очистки консоли
def clear(): return os.system('cls')

def read_string(data_file):
    with open(data_file,'r') as data:
        return data.readline()
           
def append_polynomial_to_file(polinomial, filename):
    with open(filename,'a') as data:
        data.write(polinomial) 

def fill_coefficients(polynomial):
    coefficients_list = []
    coefficients_list = polynomial.split(' ')
    for i in range (len(coefficients_list)):
        if coefficients_list[i].isdigit():
            coefficients_list[i] += '*x^0'
        if coefficients_list[i] == 'x':
            coefficients_list[i] = '1*x^1'
        if coefficients_list[i] == '+':
            coefficients_list[i] = '*x^'
        if coefficients_list[i] == '-':
            coefficients_list[i] = '*x^-'
        if 'x^' in coefficients_list[i] and '*x^' not in coefficients_list[i]:
            coefficients_list[i] = '1*' + coefficients_list[i]
        if '*x' in coefficients_list[i] and '*x^' not in coefficients_list[i]:
            coefficients_list[i] += '^1'
    if coefficients_list[-2] and coefficients_list[-1]  == '=' or '0\n':
            coefficients_list.pop()
            coefficients_list.pop()
    polynomial = ''.join(coefficients_list)
    coefficients_list = polynomial.split('*x^')
    return coefficients_list

def sum_coefficents(coefficients1, coefficients2, k):
    answer_list = []
    all_coef1 = []
    all_coef2 = []
    j = 1
    for i in range (k, -1, -1):
        if i == int(coefficients1[j]):
            all_coef1.append(int(coefficients1[j-1]))
            j += 2
        else:
            all_coef1.append(0)
        

    while len(coefficients2) < len(coefficients1):
        coefficients2.append('0')
    j = 1
    for i in range (k, -1, -1):
        if i == int(coefficients2[j]):
            all_coef2.append(int(coefficients2[j-1]))
            j += 2
        else:
            all_coef2.append(0)
    for i in range (k, -1, -1):
        answer_list.append(all_coef1[k - i] + all_coef2[k - i])  
    return answer_list
    
def create_polynomial(coefficients, k):
    answer = ''
    for i in range(k, -1, -1):
        if i == 0:
            add_part = str(coefficients[k-i]) + ' = 0\n'
        elif coefficients[k-i] == 1 and i != 1:
            add_part = 'x^' + str(i) + ' + '
        elif coefficients[k-i] == 1 and i == 1:
            add_part = 'x + '
        elif i == 1 and coefficients[k-i] != 0:
            add_part = str(coefficients[k-i]) + 'x + '
        elif coefficients[k-i] == 0:
            add_part = ''
        else:
         add_part = str(coefficients[k-i]) + 'x^' + str(i) + ' + '
        answer += add_part
    answer = answer.replace('+ 0 = 0','= 0')
    return answer

def find_k(coefficients):
    list_of_degrees = []
    for i in range (1,len(coefficients), 2):
        list_of_degrees.append(coefficients[i])
    return int(max(list_of_degrees))

while True:
    clear()    
    print('Даны два файла, в каждом из которых находится запись многочлена.\
    Программа формирует файл sum_polynomials.txt, содержащий сумму многочленов.')
    polynomial_1 = read_string('file_with_polynomials1.txt')
    polynomial_2 = read_string('file_with_polynomials2.txt')
    print(f'1 -> {polynomial_1}')
    print(f'2 -> {polynomial_2}')
    coefficients1 = fill_coefficients(polynomial_1)
    coefficients2 = fill_coefficients(polynomial_2)
    if find_k(coefficients2) > find_k(coefficients1):
        coefficients1,coefficients2 = coefficients2, coefficients1
    k = max(find_k(coefficients1), find_k(coefficients2))
    answer_coefficents = sum_coefficents(coefficients1,coefficients2, k)
    answer = create_polynomial(answer_coefficents, k)
    print(f'Ответ -> {answer}')
    append_polynomial_to_file(answer,'sum_of_polynomials.txt')
    decision = input('Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
        break
