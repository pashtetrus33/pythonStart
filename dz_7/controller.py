import imp
import os
from time import sleep
import model
import view
import text_file_creater as txt
import html_file_creater as html
from progress.bar import ShadyBar
from emoji import emojize

FILENAME_CSV = 'dz_7\\phonebook.csv'
FILENAME_TXT = 'dz_7\\phonebook.txt'
FILENAME_HTML = 'dz_7\\phonebook.html'

def clear(): return os.system('cls')

def show_menu() -> int:
    print(emojize("\nВыберите необходимое действие:\n"
          "1. :point_right: Отобразить весь справочник\n"
          "2. :mag: Найти абонента по фамилии\n"
          "3. :mag::telephone_receiver: Найти абонента по номеру телефона\n"
          "4. :person_with_blond_hair: Добавить абонента в справочник\n"
          "5. :closed_book: Сохранить справочник в текстовом формате\n"
          "6. :blue_book: Сохранить справочник в html формате\n"
          "7. :family: Добавить в справочник рандомные записи\n"
          "8. :scissors: Очистить весь справочник\n"
          "9. :checkered_flag: Закончить работу", language='alias'))
    
    choice = model.input_check()
    switch_choice(choice)

def switch_choice(choice):
    if choice == 1:
        view.phone_book(FILENAME_CSV)
        show_menu()
    elif choice == 2:
        view.find_by_surname(FILENAME_CSV)
        show_menu()
    elif choice == 3:
        view.find_by_phone(FILENAME_CSV)
        show_menu()
    elif choice == 4:
        data = view.add_record()
        model.write_csv(FILENAME_CSV,'a', data)
        show_menu()
    elif choice == 5:
        data = model.read_csv(FILENAME_CSV)
        txt.write_txt(FILENAME_TXT, 'w',data)
        show_menu()
    elif choice == 6:
        data = model.read_csv(FILENAME_CSV)
        html.write_html(FILENAME_HTML, 'w', data)
        show_menu()
    elif choice == 7:
        n = model.input_int()
        bar = ShadyBar('Processing', max = n)
        for i in range(n):
            data = view.add_random_record()
            model.write_csv(FILENAME_CSV,'a', data)
        for i in range(n):
            sleep(0.05)
            bar.next()
        bar.finish()
        show_menu()
    elif choice == 8:
        model.write_csv(FILENAME_CSV,'w')
        show_menu()
    elif choice == 9:
        view.exit()
        