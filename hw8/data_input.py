from datetime import datetime
import datetime

def record():
    entry = []
    surname = input('Введите фамилию: ')
    entry.append(surname.title())
    name = input('Введите имя: ')
    entry.append(name.title())
    phone_num = input('Введите номер телефона: ')
    entry.append(phone_num)
    description = input('Введите описание контакта (Личный, Рабочий, Домашний и т.д.): ')
    entry.append(description.title())
    dt = datetime.datetime.now()
    entry.insert(0, dt.strftime('%H:%M - %d.%m.%Y год'))
    print('Вами введена запись: ', entry)
    return entry
