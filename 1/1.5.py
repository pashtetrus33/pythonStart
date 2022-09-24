# Задача 5: Программа для проверки истинности утверждения !(X V Y V Z) = !X /\ !Y /\ !Z для всех значений предикат.

import os
from time import sleep
clear = lambda: os.system('cls')
clear()  # очистка консоли
print('Программа для проверки истинности утверждения !(X V Y V Z) = !X /\ !Y /\ !Z для всех значений предикат.')
print()
for x in range(0,2):
    for y in range (0,2):
        for z in range(0,2):
            print()
            if not (x or y or z) == (not x and not y and not z):
                sleep(1) 
                print (f'Для X = {x}, Y = {y}, Z = {z} -> Утверждение истинно!')
            else:
                print (f'Для X = {x}, Y = {y}, Z = {z} -> Утверждение ложно!')
print()