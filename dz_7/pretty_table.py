from prettytable import PrettyTable
import model

def table_print(data):
    x = PrettyTable()
    x.field_names = model.fields
    
    for dict in data:
        x.add_row(dict.values())
    print(x)