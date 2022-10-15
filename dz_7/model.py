
from time import sleep
import controller


fields = ["Фамилия", "Имя", "Телефон", "Дата рождения", "Описание"]
def input_check():  
    while True:
        s = input(': ')
        try:
            if int(s) > 0 and int(s) < 10:
                return int(s)
            else:
                print('Ошибка. Ожидалось целое число от 1 до 9.')
            
        except ValueError:
            print('Ошибка. Ожидалось целое число от 1 до 9.')

def input_int():  
    while True:
        s = input('Введите количество создаваемых записей: ')
        try:
            if int(s) > 0:
                return int(s)
            else:
                print('Ошибка. Ожидалось целое число больше 0.')    
        except ValueError:
            print('Ошибка. Ожидалось целое число больше 0.')
            

def save_txt_format():
    return None


def read_csv(filename: str) -> list:
    data = []
    global fields
    try:
        with open(filename, 'r', encoding='utf-8') as f_in:
            for line in f_in:
                record = dict(zip(fields, line.strip().split(',')))
                data.append(record)
            return data
    except IOError:
            sleep(0.5)
            print(f'Ошибка. Файл {filename} не найден!')
            sleep(1)
            controller.show_menu()


def write_csv(filename,mode, data = None):
    with open(filename, mode, encoding= 'utf-8') as file:
        if data != None:
            file.write('{},{},{},{},{},\n'.format(data[0],data[1], data[2],data[3],data[4]))
        else:
            sleep(1)
            print('Cправочник очищен')
            sleep(1)
            file.close()
    
