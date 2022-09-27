# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

import os
from time import sleep
def clear(): return os.system('cls')


clear()  # очистка консоли


def inputFloat(prompt=None):  # метод проверки на ввод вещественного числа
    while True:
        s = input(prompt)
        try:
            return float(s)
        except ValueError:
            print('Ошибка. Ожидалось вещественное число.')
            sleep(2)
            clear()


while True:
    float_number = inputFloat('Программа принимает на вход вещественное число и показывает сумму его цифр.\nВведите вещественное число: ')
    origin = float_number
    while float_number - int(float_number) != 0:
        float_number *= 10
        # если не округлять, то в связи с особенностями хранения вещественных чисел в памяти будет не то что мы предполагаем.
        float_number = round(float_number, 8)
    int_number = int(float_number)
    sum = 0
    while int_number != 0:
        sum += int_number % 10
        # целочисленное деление на 10 (отбрасывает последнюю цифру)
        int_number //= 10
    print(f'Cумма цифр вещественного числа {origin} = {sum}')
    decision = input(
        'Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
        break
