def choose_menu():
    print('Вас приветствует телефонный справочник.')
    menu_choice = int(input('Выберите пункт меню:\n\
        1 - Внести данные\n\
        2 - Поиск\n\
        3 - Показать все данные\n\
        4 - Выход\n\
        Ваш выбор: '))
    return menu_choice

def choose_style():
    n = int(input('В каком формате показать данные: \n\
        1 - Строка;\n\
        2 - Столбец.\n\
        Ваш выбор: '))
    return n