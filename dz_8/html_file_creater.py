from time import sleep

def write_html(filename,mode, data):
    page = open(filename, mode, encoding= 'utf-8')
    for dict in data:
        style = 'style="font-size:30px;"'
        html = '<html>\n  <head></head>\n  <body>\n'
        html += '    <p {}>Фамилия: {}</p>\n'\
            .format(style,dict['Фамилия'])
        html += '    <p {}>Имя: {}</p>\n'\
            .format(style,dict['Имя'])
        html += '    <p {}>Факультет: {}</p>\n'\
            .format(style, dict['Факультет'])
        html += '    <p {}>Курс: {}</p>\n'\
            .format(style, dict['Курс'])
        html += '    <p {}>Успеваемость: {}</p>\n'\
            .format(style, dict['Успеваемость'])
        html += '    <p {}>Дата рождения: {}</p>\n'\
            .format(style, dict['Дата рождения'])
        html += '    <p {}>Телефон: {}</p>\n'\
            .format(style, dict['Телефон'])
        html += '  </body>\n</html>\n'
        
        page.write(f"{html}\n") 

    page.close()
    sleep(1)
    print(f'HTML файл {filename} записан.')
    sleep(1)
    return data