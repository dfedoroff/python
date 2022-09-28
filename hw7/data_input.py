def input_data():
    name = input('Имя: ')
    surname = input('Фамилия: ')
    phone = input('Номер телефона: ')
    comment = input('Комментарий: ')
    return [name, surname, phone, comment]

def write_in_row(data):
    str = ''
    for i in data:
        str += i + ';'
    str += '\n'
    with open('data_row.csv', 'a') as file:
        file.write(str)

def write_in_column(data):
    with open('data_col.csv', 'a') as file:
        for i in data:
            file.write(i)
            file.write('\n')
