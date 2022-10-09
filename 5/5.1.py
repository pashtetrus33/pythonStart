# Задача 1.Напишите программу, удаляющую из текста все слова, содержащие ""абв""

import os
from random import choices
from time import sleep

# метод очистки консоли
def clear(): return os.system('cls')

def create_text(length, word_size, alphabet):
    text = ''
    for i in range(length):
        word = choices(alphabet, k = word_size)
        word = ''.join(word)
        text += word + " "
    return text
def write_text_to_file(text, filename):
    with open(filename,'w', encoding= 'utf-8') as data:
        data.write(text)

def read_text_from_file(data_file):
    text = ''
    with open(data_file,'r', encoding= 'utf_8') as data:
        for line in data:
            text +=line
        return text 
       
while True:
    clear()   
    print('Программа удаляет из текста все слова, содержащие "абв"')   
    #Генерация текста, первый аргумент - число слов, второй - длина слова, третий - алфавит
    text = create_text(20,3,'абв')
    write_text_to_file(text, 'text.txt')
    text = read_text_from_file('text.txt').split()
    print(f'Текст до (кол-во слов: {len(text)}): {text}' )
    search_word = 'абв'
    #Cпособ 1
    #original_text = deepcopy(text)
    # for word in original_text:
    #     if word.count(search_word) >= 1:
    #          text.remove(word)

    #Способ 2
    text = [word for word in text if 'абв' not in word]
    print(f'Текст после (кол-во слов: {len(text)}): {text}')

    decision = input('Для продолжения нажмите "ENTER", для выхода "E" затем "ENTER" ')
    clear()
    if (decision.lower() == 'e') or (decision.lower() == 'у'):
        break