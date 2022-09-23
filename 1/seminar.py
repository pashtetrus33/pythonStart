a = int(input('Введите число a '))
b = int(input('Введите число b '))

if a*a==b:
    print (f'- {a}, {b} -> да')

elif b*b==a:
    print (f'- {a}, {b} -> да')
else:
    print (f'- {a}, {b} -> нет')

#******************************************************************************************

numbers = int(input(' input amount of numbers:  '))
count = 1
arr = []
while( count <= numbers):
    num = int(input(f"input {count} number: "))
    arr.append(num)
    count += 1 
print (arr)
max_num = arr[0]
for i in arr:
    if i > max_num:
        max_num = i

print(f' max number is: {max_num}')

#****************************************************************************************

# a = int (input("введите a: "))
# b = int (input("введите b: "))
# c = int (input("введите c: "))
# d = int (input("введите d: "))
# e = int (input("введите e: "))

# m = a
# for i in b,c,d,e:
#     if i>m: m=i
# print(m)

#**************************************************************************************
a = int (input("введите a: "))
b = int (input("введите b: "))
if a*a == b or b*b==a:
    print ("да")
else:
    print ("нет")

#**************************************************************************************
print('введите числа')
value = int(input())
print (list (range(-value, value+1)))

#**************************************************************************************
f = float(input())
d = int( (f*10) % 10 )
print(f, d, sep=" -> ")

#**************************************************************************************
n = int(input())
b = (n % 5 == 0 and n % 10 ==0 or n % 15 == 0) and not n % 30 == 0
print(n, b, sep=" -> ")
