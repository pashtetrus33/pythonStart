from random import randint
from secrets import choice

MALE_NAMES = 'dz_8\\random_student\\male_names.txt'
FEMALE_NAMES = 'dz_8\\random_student\\female_names.txt'
SURNAMES = 'dz_8\\random_student\\surnames.txt'
FACULTY = 'dz_8\\random_student\\msu_fac.txt'
MARKS = 'dz_8\\random_student\\marks.txt'

def get_surname(sex):
    with open (SURNAMES,encoding="utf8") as sur:
            surnames = list(sur)
    if sex:
        return choice(surnames)[:-1]
    else:
        female_sur = choice(surnames)[:-1] + 'а'
        return female_sur
    
def get_name(sex):
    if sex == 1: 
        with open (MALE_NAMES,encoding="utf8") as f:
            names = list(f)         
    else:
        with open (FEMALE_NAMES,encoding="utf8") as f:
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
        year = randint (2001, 2005)
        return str(day) + '.' + str(month) + '.' + str(year)

def get_faculty():
    with open (FACULTY,encoding="utf8") as f:
            fac = list(f)    
    return choice(fac)[:-1]

def get_course(data):
    course = 0
    if int((data[-4:])) == 2005:
        course = 1
    elif int((data[-4:])) == 2004:
        course = 2
    elif int((data[-4:])) == 2003:
        course = 3
    elif int((data[-4:])) == 2002:
        course = 4
    elif int((data[-4:])) == 2001:
        course = 5
    else:
        course = randint(1,5)    
    return course

def get_description():
    with open (MARKS,encoding="utf8") as f:
            marks = list(f)    
    return choice(marks)[:-1]


def data_collection():
    sex = randint(0,1)
    data = []
    data.append(get_surname(sex))
    data.append(get_name(sex))
    birth = get_birth_date()
    data.append(get_faculty())
    data.append(get_course(birth))
    data.append(get_description())
    data.append(birth)
    data.append(get_phone())
    return data