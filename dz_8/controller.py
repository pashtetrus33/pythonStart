import os
import model
import view
import text_file_creater as txt
import html_file_creater as html

FILENAME_CSV = 'dz_8\\students.csv'
FILENAME_TXT = 'dz_8\\students.txt'
FILENAME_HTML = 'dz_8\\students.html'

def clear(): return os.system('cls')

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
           "1.  Отобразить всех студентов\n"
           "2.  Найти студента по фамилии\n"
           "3.  Найти студента по номеру телефона\n"
           "4.  Найти студентов по факультету\n"
           "5.  Найти студентов по успеваемости\n"
           "6.  Найти студентов по номеру курса\n"
           "7.  Добавить студента в справочник\n"
           "8.  Сохранить список студентов в текстовом формате\n"
           "9.  Сохранить список студентов в html формате\n"
          "10. Отобразить данные из текстового формата\n"
          "11. Добавить в список студентов рандомные записи\n"
          "12. Очистить весь список\n"
          "13. Закончить работу")
    
    choice = model.input_check()
    switch_choice(choice)

def switch_choice(choice):
    if choice == 1:
        view.view_students(FILENAME_CSV)
        show_menu()
    elif choice == 2:
        view.find_by_surname(FILENAME_CSV)
        show_menu()
    elif choice == 3:
        view.find_by_phone(FILENAME_CSV)
        show_menu()
    elif choice == 4:
        view.find_by_fac(FILENAME_CSV)
        show_menu()
    elif choice == 5:
        view.find_by_marks(FILENAME_CSV)
        show_menu()
    elif choice == 6:
        view.find_by_course(FILENAME_CSV)
        show_menu()
    elif choice == 7:
        data = view.add_record()
        model.write_csv(FILENAME_CSV,'a', data)
        show_menu()
    elif choice == 8:
        data = model.read_csv(FILENAME_CSV)
        txt.write_txt(FILENAME_TXT, 'w',data)
        show_menu()
    elif choice == 9:
        data = model.read_csv(FILENAME_CSV)
        html.write_html(FILENAME_HTML, 'w', data)
        show_menu()
    elif choice == 10:
        view.view_txt(FILENAME_TXT)
        show_menu()
    elif choice == 11:
        n = model.input_int()
        for i in range(n):
            data = view.add_random_record()
            print('Запись(и) добавлена(ы).')
            model.write_csv(FILENAME_CSV,'a', data)
        show_menu()
    elif choice == 12:
        model.write_csv(FILENAME_CSV,'w')
        show_menu()
    elif choice == 13:
        view.exit()
        