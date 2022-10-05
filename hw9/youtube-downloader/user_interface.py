def select_item():
    while True:
        menu_choice = ('1 - Загрузить видео',
                       '2 - Загрузить аудио',
                       '3 - Выход')
        for item in menu_choice:
            print(item)
        num = input('Выберите пункт меню: ')
        menu = '123'
        if num in menu:
            return num
        else:
            print('Неверный ввод!', '\n')
