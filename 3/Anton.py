# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

strings= ['osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen', 'anton', 'aoooooooooontooooo', 'elelelelelelelelelel', 'ntoneeee', 'tonee', '253235235a5323352n25235352t253523523235oo235523523523n', 'antoooooooooooooooooooooooooooooooooooooooooooooooooooon', 'unton', 'notna', 'a1n2t3o4n5']
hacker =  ['a', 'n', 't', 'o', 'n']
count=0
otvet=[]

for string in strings:
    index =0
    for c in hacker:
        for i in range(index, len(string)):
            if c == string[i]:
                count += 1
                #print(f'Буква {c} = {string[i]}  Count = {count}')
                index = i
                break   
    if count == 5:
        otvet.append(strings.index(string) + 1)
    count = 0
print(f'Результат: {otvet}')