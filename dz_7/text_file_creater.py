from time import sleep

def write_txt(filename,mode, data):
    with open(filename, mode, encoding= 'utf-8') as file:
        if data != None:
            for dict in data:
                for item in dict:
                    file.write(f"{dict[item]}\n")
                file.write(f"\n") 
            sleep(1)
            print(f'Текстовый файл {filename} записан.')
            sleep(1)
    return data