from random import randint

# Метод выбора ботом количества конфет
def bot_choice(filled_cells, filled_cells_player_1):
    
    if len(filled_cells) == 0 or is_empty(5,filled_cells):
        bot_choice = 5
    elif 1 in filled_cells_player_1 and 4 in filled_cells_player_1 and is_empty(7,filled_cells):
        bot_choice = 7
    elif 1 in filled_cells_player_1 and 7 in filled_cells_player_1 and is_empty(4,filled_cells):
        bot_choice = 4
    elif 4 in filled_cells_player_1 and 7 in filled_cells_player_1 and is_empty(1,filled_cells):
        bot_choice = 1
    elif 2 in filled_cells_player_1 and 5 in filled_cells_player_1 and is_empty(8,filled_cells):
        bot_choice = 8
    elif 2 in filled_cells_player_1 and 8 in filled_cells_player_1 and is_empty(5,filled_cells):
        bot_choice = 5
    elif 5 in filled_cells_player_1 and 8 in filled_cells_player_1 and is_empty(2,filled_cells):
        bot_choice = 2
    elif 3 in filled_cells_player_1 and 6 in filled_cells_player_1 and is_empty(9,filled_cells):
        bot_choice = 9
    elif 3 in filled_cells_player_1 and 9 in filled_cells_player_1 and is_empty(6,filled_cells):
        bot_choice = 6
    elif 6 in filled_cells_player_1 and 9 in filled_cells_player_1 and is_empty(3,filled_cells):
        bot_choice = 3
    elif 1 in filled_cells_player_1 and 5 in filled_cells_player_1 and is_empty(9,filled_cells):
        bot_choice = 9
    elif 1 in filled_cells_player_1 and 9 in filled_cells_player_1 and is_empty(5,filled_cells):
        bot_choice = 5
    elif 5 in filled_cells_player_1 and 9 in filled_cells_player_1 and is_empty(1,filled_cells):
        bot_choice = 1
    elif 7 in filled_cells_player_1 and 5 in filled_cells_player_1 and is_empty(3,filled_cells):
        bot_choice = 3
    elif 7 in filled_cells_player_1 and 3 in filled_cells_player_1 and is_empty(5,filled_cells):
        bot_choice = 5
    elif 5 in filled_cells_player_1 and 3 in filled_cells_player_1 and is_empty(7,filled_cells):
        bot_choice = 7
    elif 1 in filled_cells_player_1 and 2 in filled_cells_player_1 and is_empty(3,filled_cells):
        bot_choice = 3
    elif 1 in filled_cells_player_1 and 3 in filled_cells_player_1 and is_empty(2,filled_cells):
        bot_choice = 2
    elif 2 in filled_cells_player_1 and 3 in filled_cells_player_1 and is_empty(1,filled_cells):
        bot_choice = 1
    elif 4 in filled_cells_player_1 and 5 in filled_cells_player_1 and is_empty(6,filled_cells):
        bot_choice = 6
    elif 4 in filled_cells_player_1 and 6 in filled_cells_player_1 and is_empty(5,filled_cells):
        bot_choice = 5
    elif 5 in filled_cells_player_1 and 6 in filled_cells_player_1 and is_empty(4,filled_cells):
        bot_choice = 4
    elif 7 in filled_cells_player_1 and 8 in filled_cells_player_1 and is_empty(9,filled_cells):
        bot_choice = 9
    elif 7 in filled_cells_player_1 and 9 in filled_cells_player_1 and is_empty(8,filled_cells):
        bot_choice = 8
    elif 8 in filled_cells_player_1 and 9 in filled_cells_player_1 and is_empty(7,filled_cells):
        bot_choice = 7
    else:
        while True: 
            bot_choice = randint(1,9)  
            if bot_choice not in filled_cells: 
                break  
    return bot_choice
#  Метод проверки занята клетка или нет
def is_empty(choice, filled_cells):
    my_dict = {'a1':1,'a2':4,'a3':7,'b1':2,'b2':5,'b3':8,'c1':3,'c2':6,'c3':9}
    if type(choice) == int:
        return not choice in filled_cells
    else:
        return not my_dict[choice] in filled_cells
     
