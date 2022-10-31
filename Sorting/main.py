from random import randint
from quick_sort import quicksort

from visualizing_bubble_sort_matplotlib import visualize_matplotlib

#SORT_METHOD = 'bubble_sort'
#SORT_METHOD = 'selection_sort'
SORT_METHOD = 'quick_sort'

n  = int(input("Введите кол-во элементов массива: "))

#sort_type True по возрастанию, False по убыванию
sort_type  = int(input("Cортировка по возрастанию 1 по убыванию 0: "))

# Заполнение массива
#Ручное заполнение
#array = [input('Введите число: ') for _ in range(n)]
# Рандомное заполнение вариант 1:
# N = 30
# A = list(range(1, N + 1))
#random.shuffle(A)

# Рандомное заполнение вариант 2:
array = [randint(1,100) for _ in range(n)]

print(f'\nНачальный массив:                   {array}')

visualize_matplotlib(array,SORT_METHOD, sort_type)


if sort_type:
	print(f'Массив отсортирован по возрастанию: {array}\n')
else:
	print(f'Массив отсортирован по убыванию:    {array}\n')
		
