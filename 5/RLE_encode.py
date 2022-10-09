# Модуль для сжатия по RLE алгоритму
# Честно подсмотрел погуглив (ломал голову весь день :)
def RLE_text_encode(in_text):
    out_text = []
    for message in in_text:
        encoded_string = ""
        i = 0
        while (i <= len(message)-1):
            count = 1
            ch = message[i]
            j = i
            while (j < len(message)-1):   
                if (message[j] == message[j + 1]): 
                    count = count + 1
                    j = j + 1
                else: 
                    break
            encoded_string = encoded_string + str(count) + ch
            i = j + 1
        out_text.append(encoded_string + " ")
    return out_text