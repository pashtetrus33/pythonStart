# Задача 3. Создайте программу для игры в ""Крестики-нолики""
# Подглядел в интернете, но разобрался :)

from time import sleep, time
from random import choice
from tkinter import *

def win(n):
    global game
    if (game[0] == n and game[1] == n and game[2] == n) or (game[3] == n and game[4] == n and game[5] == n) or (game[6] == n and game[7] == n and game[8] == n) or (game[0] == n and game[3] == n and game[6] == n) or (game[1] == n and game[4] == n and game[7] == n) or (game[2] == n and game[5] == n and game[8] == n) or (game[0] == n and game[4] == n and game[8] == n) or (game[2] == n and game[4] == n and game[6] == n):
        return True

def stop_game():
    global game_left
    for item in game_left:
        buttons[item].config(bg='white',state='disabled')

def push(b):
    global game
    global game_left
    global turn
    game[b] = 'X'
    buttons[b].config(text='X',bg='white',state='disabled')
    game_left.remove(b)
    if b == 4 and turn == 0:
        t = choice(game_left)     
    elif b != 4 and turn == 0:
        t = 4 
    if turn > 0:
            t = 8 - b
    if t not in game_left:
        try:
            t = choice(game_left) 
        except IndexError:
             label['text'] = 'Ничья!'
             stop_game()
         
    game[t] = '0'
    sleep(0.5)
    buttons[t].config(text='0',bg='white',state='disabled')
    if win('X'):
        label['text'] = 'Вы выиграли!'
        stop_game()
    elif win('0'):
         label['text'] = 'Вы проиграли!'
         stop_game()
    else:
        if len(game_left) >=1:
            game_left.remove(t)
        else:
            label['text'] = 'Ничья!'
            stop_game()
        turn += 1          
turn = 0
game = [None]*9
game_left = list(range(9))
root = Tk()
label = Label(width=20, text="Tic Tac Toe", font=('Arial',20,'bold'))
buttons = [Button(width= 5, height= 2, font=('Arial',28,'bold'),bg='blue', command= lambda x=i: push(x)) for i in range(9)]
label.grid(row=0, column=0, columnspan=3)
r = 1
col = 0
for i in range(9):
    buttons[i].grid(row= r, column= col)
    col += 1
    if col == 3:
        r +=1
        col = 0   
root.mainloop()