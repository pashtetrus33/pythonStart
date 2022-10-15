import controller
import model
import random_person.person_generator as rp
from time import sleep


# Пункт меню: 1
def phone_book(filename):
    print('\nВывод всего справочника:\n')
    data = model.read_csv(filename)
    if len(data) == 0:
        print('Cправочник пустой.')
    for i, dict in enumerate(data):
        print('{:3d}'.format(i+1), end= ': ')
        for item in dict:
            print('{:15s}{:15s}'.format(item, dict[item]),end=" ")
        print('\n')
      
# Пункт меню: 2
def find_by_surname(filename):
    found = False
    surname = input('Введите фамилию для поиска: ')
    data = model.read_csv(filename)
    for i, dict in enumerate(data):
        if surname ==  dict.get('Фамилия'):
            print(i+1)
            found = True
            for item in dict:
                sleep(0.05)
                print('{:15s}{:15s}'.format(item, dict[item]))
            print()
    if not found:
        sleep(0.5)
        print('Записей не найдено.\n')


# Пункт меню: 3
def find_by_phone(filename):
    found = False
    phone = input('Введите телефон для поиска: ')
    data = model.read_csv(filename)
    for i, dict in enumerate(data):
        if phone ==  dict.get('Телефон'):
            print(i+1)
            found = True
            for item in dict:
                sleep(0.05)
                print('{:15s}{:15s}'.format(item, dict[item]))
            print()
    if not found:
        sleep(0.5)
        print('Записей не найдено.\n')


# Пункт меню: 4
def add_record():
    manual_record = []
    print('Для добавления записи в телефонный справочник введите данные:')
    manual_record.append(input('Введите фамилию: '))
    manual_record.append(input('Введите имя: '))
    manual_record.append(input('Введите телефон: '))
    manual_record.append(input('Введите дату рождения: '))
    manual_record.append(input('Введите описание: '))
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