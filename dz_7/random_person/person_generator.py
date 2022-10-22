from random import randint
from secrets import choice


def get_surname(sex):
    with open ('dz_7\\random_person\\surnames.txt',encoding="utf8") as sur:
        surnames = list(sur)
    if sex:
        return choice(surnames)[:-1]
    else:
        female_sur = choice(surnames)[:-1] + 'а'
        return female_sur
    
def get_name(sex):
    if sex == 1: 
        with open ('dz_7\\random_person\\male_names.txt',encoding="utf8") as f:
            names = list(f)         
    else:
        with open ('dz_7\\random_person\\female_names.txt',encoding="utf8") as f:
            names = list(f)    
    return choice(names)[:-1]


def get_phone():
        country_id = randint(1, 99)
        city_id = randint(100, 500)
        phone_id = randint (100000, 1000000)
        return '+' + str(country_id) + '-' + str(city_id) + '-' + str(phone_id)


def get_birth_date():
        day = randint(1, 30)
        month = randint(1, 12)
        year = randint (1951, 2004)
        return str(day) + '.' + str(month) + '.' + str(year)


def get_description():
    with open ('dz_7\\random_person\\descriptions.txt',encoding="utf8") as f:
            professions = list(f)    
    return choice(professions)[:-1]


def data_collection():
    sex = randint(0,1)
    return [get_surname(sex), get_name(sex), get_phone(), get_birth_date(), get_description()]