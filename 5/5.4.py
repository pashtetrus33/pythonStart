# Задача 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
from RLE_encode import RLE_text_encode
from RLE_decode import RLE_text_decode

def read_file(file_name):
    f = open(file_name, 'r' , encoding= 'utf-8')
    data = f.read() + ' '
    f.close
    words= []
    while data != '':
        space_pos = data.index(' ')
        words.append(data[:space_pos])
        data = data[space_pos+1:]
    return words

def write_file(file_name, RLE_text):
    with open(file_name,'w', encoding= 'utf-8') as data:
         for i in RLE_text:
            data.write(i + '')

    
original_text = read_file('5_4.txt')
zipped_text = RLE_text_encode(original_text)
write_file('5_4_encoded.txt', zipped_text)
zipped_text = read_file('5_4_encoded.txt')
unzipped_text = RLE_text_decode(zipped_text)
write_file('5_4_decoded.txt',unzipped_text)
