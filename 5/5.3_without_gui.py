# Задача 3. Создайте программу для игры в ""Крестики-нолики"".
import os
from time import sleep, time
from random import randint
from tic_tac_toe_check_input import check_input
from tic_tac_toe_is_winner import is_winner
from tic_tac_toe_bot_choice import is_empty
from tic_tac_toe_bot_choice import bot_choice

board = [" "]*9
my_dict = {'a1':1,'a2':4,'a3':7,'b1':2,'b2':5,'b3':8,'c1':3,'c2':6,'c3':9}
bot_dict = {1:'a1',2:'b1',3:'c1',4:'a2',5:'b2',6:'c2',7:'a3',8:'b3',9:'c3'}
# Метод очистки консоли
def clear(): return os.system('cls')
def print_field():
    print("-" * 16)
    print("     a   b   c")
    for i in range(3):
        print(f" {i+1} |", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 16)
# Основный цикл
while True:
    clear()   
    print(f'########################  Игра "крестики - нолики"  ##########################\nПервый ход крестиками определяется жеребьёвкой.\n')   
    sleep(2)
    print('Жеребъевка\n')
    sleep(2)
    # Случайный выбор чей первый ход
    if  randint(0,1):
        current_player = 1
        print('Человек ходит первый.\n')
     
    else:
        current_player = 2
        print('Бот ходит первый.\n')
    filled_cells = []
    filled_cells_player_1 = []
    filled_cells_player_2 = []
    print_field()
    # Основной цикл игры
    while True:
        if current_player == 1:
            current_player_choice = check_input(filled_cells,'Ход Человека: ')
            current_player_choice = my_dict[current_player_choice]
            filled_cells_player_1.append(current_player_choice)   
        else:
            current_player_choice = bot_choice(filled_cells, filled_cells_player_1)
            print(f'Ход Бота: {bot_dict[current_player_choice]}')
            filled_cells_player_2.append(current_player_choice)
        
        filled_cells.append(current_player_choice)
        if current_player == 1:
            board[current_player_choice - 1] = 'X'
        else:
            board[current_player_choice - 1] = '0'
        #проверка выигрыша 
        print_field()   
        if is_winner(filled_cells,filled_cells_player_1,filled_cells_player_2, current_player):
            break
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1
    decision = input('Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    board = [" "]*9
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
         break