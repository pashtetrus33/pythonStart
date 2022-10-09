# Модуль для распаковки по RLE алгоритму
# Честно подсмотрел погуглив (ломал голову весь день :)
def RLE_text_decode(in_text):
    out_text = []
    for message in in_text:
        decoded_message = ""
        i = 0
        j = 0
        while (i <= len(message) - 1):
            run_count = int(message[i])
            run_word = message[i + 1]
            for j in range(run_count):
                decoded_message = decoded_message+run_word
                j = j + 1
            i = i + 2
        out_text.append(decoded_message + " ")
    return out_text