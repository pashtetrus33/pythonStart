# Задача 2.Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import os
from random import randint
from time import sleep, time

# Вводим константы
CANDIES = 125
MAX_CANDIES =28
# Метод очистки консоли
def clear(): return os.system('cls')
# Метод проверки корректного ввода количества конфет
def input_legitime(prompt=None):  
    while True:
        s = input(prompt)
        try:
            if int(s) > 0 and int(s) < MAX_CANDIES + 1:
                return int(s)
            else:
                print(f'Ошибка. Ожидалось 0 < целое число < {MAX_CANDIES + 1}.')
                sleep(2)
                clear()
        except ValueError:
            print(f'Ошибка. Ожидалось 0 < целое число < {MAX_CANDIES + 1}.')
            sleep(2)
            clear()
# Метод проверки ввода режима работы программы
def input_mode(prompt=None):  
    while True:
        s = input(prompt)
        try:
            if int(s) == 0 or int(s) == 1:
                return int(s)
            else:
                print('Ошибка. Ожидалось 0 или 1.')
                sleep(2)
                clear()
        except ValueError:
            print('Ошибка. Ожидалось 0 или 1.')
            sleep(2)
            clear()
# Метод выбора ботом количества конфет
def bot_choice(player1_ammount, candies_ammount):
    #return randint(1,28)  Вариант для глупого бота
    if candies_ammount <= MAX_CANDIES:
        return candies_ammount
    elif candies_ammount == CANDIES:
        return CANDIES % (MAX_CANDIES + 1)
    else:
        if candies_ammount % (MAX_CANDIES + 1) != 0:
            return candies_ammount % (MAX_CANDIES + 1)
        else:
            return randint(1,28)
# Основный цикл
while True:
    clear()   
    print(f'########################  Игра с конфетами  ##########################\nНа столе лежит {CANDIES} конфет(а).\nИграют два игрока или игрок против бота делая ход друг после друга.\nПервый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем {MAX_CANDIES} конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.')   
    isPlayer1 = False
    isPlayer2 = False
    candies_ammount = CANDIES
    player1_ammount = 0
    player2_ammount = 0
    sleep(1)
    game_mode_choice = input_mode(f'\nДля игры с человеком нажмите "0" с ботом "1": ')
    print('Жеребъевка\n')
    sleep(2)
    # Случайный выбор чей первый ход
    if  randint(0,1):
        isPlayer1 = True
        current_player = 1
        if (game_mode_choice):
            print('Человек ходит первый!\n')
        else:
            print('Игрок 1 ходит первый!\n')
    else:
        isPlayer2 = True
        current_player = 2
        if (game_mode_choice):
            print('Бот ходит первый!\n')
        else:
            print('Игрок 2 ходит первый!\n')
    # Основной цикл игры
    while True:
        
        current_player_turn = candies_ammount +1
        
        while candies_ammount - current_player_turn < 0:
            if game_mode_choice == 0:
                current_player_turn = input_legitime(f'Игрок {current_player} Введите количество конфет от 1 до {MAX_CANDIES}: ')
            else:
                if current_player == 1:
                    current_player_turn = input_legitime(f'Человек, введите количество конфет от 1 до {MAX_CANDIES}: ')
                else:
                    current_player_turn = bot_choice(player1_ammount, candies_ammount)
                    print (f'Бот сделал ход: {current_player_turn}') 

            if candies_ammount - current_player_turn < 0:
                print(f'Вы пытаетесь взять больше конфет чем есть на столе {current_player_turn} > {candies_ammount} !')
        if candies_ammount - current_player_turn == 0:
            sleep(2)
            print('\nПоздравляем!')
            if game_mode_choice == 0:
                print(f'Выиграл игрок {current_player} он забирает все конфеты оппонента\n')
            else:
                if current_player == 1:
                    print(f'Выиграл Человек он забирает все конфеты Бота\n')
                else:
                     print(f'Выиграл Бот он забирает все конфеты Человека\n')
            break
        
        if (current_player == 1):
            player1_ammount += current_player_turn
            current_player = 2
        else:
            player2_ammount += current_player_turn
            current_player = 1
        candies_ammount -= current_player_turn
        if game_mode_choice == 0:
            print(f'\nУ игрока 1: {player1_ammount} конфет(a,ы)')
            print(f'У игрока 2: {player2_ammount} конфет(а,ы)')
            print(f'\nНа столе осталось:', end=' ')
            sleep(2)
            print(f'{candies_ammount} конфет(а,ы)\n')
            sleep(2)
        else:
            print(f'\nУ Человека: {player1_ammount} конфет(a,ы)')
            print(f'У Бота: {player2_ammount} конфет(а,ы)')
            print(f'\nНа столе осталось:', end=' ')
            sleep(2)
            print(f'{candies_ammount} конфет(а,ы)\n')
            sleep(2)
 
    decision = input('Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
         break