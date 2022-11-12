#See README.MD file

from math import cos, sin
from numpy import arange
import matplotlib.pyplot as plt

MIN = -100
MAX = 100
STEP = 0.1

def prepare_data():
    f = lambda x: -12*sin(cos(x))*x**4 - 18*x**3 + 5*x**2 + 10*x - 30

    x_y_list = [(round(x,2),round(f(round(x,2)),3)) for x in arange(MIN,MAX+STEP,STEP)]
   
    return x_y_list

def draw_graph(data):
    x_list = [x[0] for x in data]
    y_list = [y[1] for y in data]
    # for i in range(len(y_list)):
    #     print(x_list[i], y_list[i], sep=' -> ')
    plt.plot(x_list,y_list)
    plt.show()
    print(f'\n4. Cтроим график (см. окно с графиком)\n')


def max_local(data):
    max_x_y = max(data, key=lambda i : i[1])
    max_x = max_x_y[0]
    max_y = max_x_y[1]
  
    print(f'5. Вычеслить вершину\nКоординаты вершины в интервале x от {MIN} до {MAX} равны x = {max_x} f(x) = {max_y}')

def increase_list(data):

    inc_list = []
    x_list = [x[0] for x in data]
    y_list = [y[1] for y in data]
    j = -1
    next_list = True
    for i in range(len(y_list) - 1):
        if y_list[i] < y_list[i+1]:
            if next_list:
                inc_list.append([])
                j += 1
                next_list = False
            inc_list[j].append(x_list[y_list.index(y_list[i])])
            inc_list[j].append(x_list[y_list.index(y_list[i+1])])
        else:
            next_list = True
            if j >= 0:
                inc_list[j] = [inc_list[j][0],inc_list[j][len(inc_list[j])-1]]
  

    print(f'\n2. Интервалы, на которых функция возрастает:\n {inc_list}')
    return inc_list

def decrease_list(data):
    dec_list = []
    x_list = [x[0] for x in data]
    y_list = [y[1] for y in data]
    j = -1
    next_list = True
    for i in range(len(y_list) - 1):
        if y_list[i] > y_list[i+1]:
            if next_list:
                dec_list.append([])
                j += 1
                next_list = False
            dec_list[j].append(x_list[y_list.index(y_list[i])])
            dec_list[j].append(x_list[y_list.index(y_list[i+1])])
        else:
            next_list = True
            if j >= 0:
                dec_list[j] = [dec_list[j][0],dec_list[j][len(dec_list[j])-1]]
    
    print(f'\n3.Интервалы, на которых функция убывает:\n {dec_list}')
    return dec_list

def f_bigger_than_0(data):

    inc_list = []
    x_list = [x[0] for x in data]
    y_list = [y[1] for y in data]
    j = -1
    next_list = True
    for i in range(len(y_list)):
        if y_list[i] > 0:
            if next_list:
                inc_list.append([])
                j += 1
                next_list = False
            inc_list[j].append(x_list[y_list.index(y_list[i])])
        else:
            next_list = True
            if j >= 0:
                inc_list[j] = [inc_list[j][0],inc_list[j][len(inc_list[j])-1]]
  

    print(f'\n6. Интервалы, на которых функция больше 0:\n {inc_list}')
    return inc_list


def f_less_than_0(data):

    inc_list = []
    x_list = [x[0] for x in data]
    y_list = [y[1] for y in data]
    j = -1
    next_list = True
    for i in range(len(y_list)):
        if y_list[i] < 0:
            if next_list:
                inc_list.append([])
                j += 1
                next_list = False
            inc_list[j].append(x_list[y_list.index(y_list[i])])
        else:
            next_list = True
            if j >= 0:
                inc_list[j] = [inc_list[j][0],inc_list[j][len(inc_list[j])-1]]
  

    print(f'\n7. Интервалы, на которых функция меньше 0:\n {inc_list}')
    return inc_list

data = prepare_data()


# 2.Найти интервалы, на которых функция возрастает
increase_list(data)

# 3.Найти интервалы, на которых функция убывает
decrease_list(data)

# 4.Построить график
draw_graph(data)

# 5.Вычислить вершину
max_local(data)

# 6.Определить промежутки, на котором f > 0
f_bigger_than_0(data)

# 7.Определить промежутки, на котором f > 0
f_less_than_0(data)

