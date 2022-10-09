# Проверка выигрыша
def is_winner (filled_cells,filled_cells_player_1,filled_cells_player_2, current_player):
    check_cells = []
    if current_player == 1:
        check_cells = filled_cells_player_1
    else:
        check_cells = filled_cells_player_2
    
    if '1' in check_cells and 4 in check_cells and 7 in check_cells  or 2 in check_cells and 5 in check_cells and 8 in check_cells or 3 in check_cells and 6 in check_cells and 9 in check_cells or 1 in check_cells and 2 in check_cells and 3 in check_cells or 4 in check_cells and 5 in check_cells and 6 in check_cells or 7 in check_cells and 8 in check_cells and 9 in check_cells or 1 in check_cells and 5 in check_cells and 9 in check_cells or 7 in check_cells and 5 in check_cells and 3 in check_cells:
        if current_player == 1:
            print(f'Поздравляем! Победил Человек.')
        else:
            print(f'Поздравляем! Победил бот.')
        return True
    elif len(filled_cells) == 9:
        print(f'Ничья!')
        return True
    else:
        return False