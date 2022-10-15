import os
import model
import view
import text_file_creater as txt
import html_file_creater as html

FILENAME_CSV = 'dz_7\\phonebook.csv'
FILENAME_TXT = 'dz_7\\phonebook.txt'
FILENAME_HTML = 'dz_7\\phonebook.html'

def clear(): return os.system('cls')

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Сохранить справочник в html формате\n"
          "7. Добавить в справочник рандомные записи\n"
          "8. Очистить весь справочник\n"
          "9. Закончить работу")
    
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
        for i in range(n):
            data = view.add_random_record()
            print('Запись(и) добавлена(ы).')
            model.write_csv(FILENAME_CSV,'a', data)
        show_menu()
    elif choice == 8:
        model.write_csv(FILENAME_CSV,'w')
        show_menu()
    elif choice == 9:
        view.exit()
        