import controller
import model
import random_student.person_generator as rp
from time import sleep
import pretty_table


# Пункт меню: 1
def view_students(filename):
    print('\nВывод всего списка студентов:\n')
    data = model.read_csv(filename)
    pretty_table.table_print(data)
    # if len(data) == 0:
    #     print('Cписок пустой.')
    # for i, dict in enumerate(data):
    #     print('{:3d}'.format(i+1), end= ': ')
    #     for item in dict:
    #         print('{:15s}{:15s}'.format(item, dict[item]),end=" ")
    #     print('\n')
    
# Пункт меню: 10
def view_txt(filename):
    print('\nВывод текстового формата:\n')
    data = model.read_txt(filename)
    pretty_table.table_print(data)
      
# Пункт меню: 2
def find_by_surname(filename):
    found = False
    surname = input('Введите фамилию для поиска: ')
    data = model.read_csv(filename)
    new_data = []
    for dict in data:
        if surname ==  dict.get('Фамилия'):
            sleep(0.05)
            new_data.append(dict)
            found = True
    pretty_table.table_print(new_data)     
    if not found:
        sleep(0.5)
        print('Записей не найдено.\n')


# Пункт меню: 3
def find_by_phone(filename):
    found = False
    phone = input('Введите телефон для поиска: ')
    data = model.read_csv(filename)
    new_data = []
    for dict in data:
        if phone ==  dict.get('Телефон'):
            sleep(0.05)
            new_data.append(dict)
            found = True
    pretty_table.table_print(new_data)   
    if not found:
        sleep(0.5)
        print('Записей не найдено.\n')


# Пункт меню: Поиск по факультету
def find_by_fac(filename):
    found = False
    phone = input('Введите факультет для поиска: ')
    data = model.read_csv(filename)
    new_data = []
    for dict in data:
        if phone ==  dict.get('Факультет'):
            sleep(0.05)
            new_data.append(dict)
            found = True
    pretty_table.table_print(new_data)   
    if not found:
        sleep(0.5)
        print('Записей не найдено.\n')

# Пункт меню: Поиск по успеваемости
def find_by_marks(filename):
    found = False
    phone = input('Введите успеваемость для поиска: ')
    data = model.read_csv(filename)
    new_data = []
    for dict in data:
        if phone ==  dict.get('Успеваемость'):
            sleep(0.05)
            new_data.append(dict)
            found = True
    pretty_table.table_print(new_data)   
    if not found:
        sleep(0.5)
        print('Записей не найдено.\n')

    # Пункт меню: Поиск по курсу
def find_by_course(filename):
    found = False
    phone = input('Введите № курса для поиска: ')
    data = model.read_csv(filename)
    new_data = []
    for dict in data:
        if phone ==  dict.get('Курс'):
            sleep(0.05)
            new_data.append(dict)
            found = True
    pretty_table.table_print(new_data)   
    if not found:
        sleep(0.5)
        print('Записей не найдено.\n')


# Пункт меню: 4
def add_record():
    manual_record = []
    print('Для добавления записи в список студентов введите данные:')
    manual_record.append(input('Введите фамилию: '))
    manual_record.append(input('Введите имя: '))
    manual_record.append(input('Введите факультет: '))
    manual_record.append(input('Введите курс: '))
    manual_record.append(input('Введите успеваемость: '))
    manual_record.append(input('Введите дату рождения: '))
    manual_record.append(input('Введите телефон: '))
    sleep(0.5)
    print('Запись добавлена.')
    return manual_record


# Пункт меню: 7
def add_random_record():
    random_record = rp.data_collection()
    return random_record

  
# Пункт меню: 9
def exit():
    print('Всего доброго, программа закрывается!')
    sleep(2)
    controller.clear()
    quit()  