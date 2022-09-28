def choose_menu():
    while True:
        menu_choice = ('1 - Ввести данные',
                       '2 - Показать данные, одна запись в строке',
                       '3 - Показать данные, каждый параметр в отдельной строке',
                       '4 - Выход')
        for i in menu_choice:
            print(i)
        num = input('Выберите пункт меню: ')
        menu = '1234'
        if num in menu:
            return num
        else:
            print('Неверный ввод!', '\n')
