# Задача 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import os
import random
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
    data_positions = []
    with open("file.txt") as f:
        for line in f:
            data_positions.append(int(line))
    number = inputInt('Программа выводит произведение элементов списка из N элементов, заполенных числами из промежтука [-N,N] на позициях, указанных в файлe file.txt.\n\nВведите число N: ')
    list_numbers = []
    for i in range (1, number +1):
        list_numbers.append(random.randint(-number,number))
    print(f'Cгенерированный список: {list_numbers}')
    print(f'Cчитанные позиции из файла: {data_positions}')

    if data_positions[0] < len(list_numbers) and data_positions[1] < len(list_numbers):
        print(f'Произведение элементов на позициях {data_positions[0]} и {data_positions[1]} =  {list_numbers[data_positions[0]]*list_numbers[data_positions[1]]}')
    else:
        print(f'Одна или обе указанные позиции отсутствует(ют) в списке!')
    
    decision = input('\n\nДля продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
        break