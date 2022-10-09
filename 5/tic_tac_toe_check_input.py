
# Метод проверки корректного ввода
from time import sleep
from tic_tac_toe_bot_choice import is_empty


def check_input(filled_cells, prompt=None):  
    while True:
        s = input(prompt)
        s = s.lower()
        if (s == 'a1' or s == 'a2' or s == 'a3' or s == 'b1' or s == 'b2' or s == 'b3' or s == 'c1' or s == 'c2' or s == 'c3'):
            if is_empty(s, filled_cells):
                return s
            else:
                print('Клетка занята!')
        else:
            print(f'Ошибка.Возможные варианты для хода: a1,a2,a3, b1,b2,b3, c1,c2,c3')
        sleep(1)
        #clear()