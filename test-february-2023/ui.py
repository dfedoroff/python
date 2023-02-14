import app


def select_menu_item():
    print('\nМеню:\n'
          '[1] Создать заметку\n'
          '[2] Прочитать заметку\n'
          '[3] Прочитать все заметки\n'
          '[4] Обновить заметку\n'
          '[5] Удалить заметку\n'
          '[6] Удалить все заметки\n'
          '[7] Выход\n'
          'Введите номер пункта меню: ', end=''
          )
    while True:
        menu_item = app.get_int_input()
        if (menu_item > 0) and (menu_item < 8):
            return menu_item
        else:
            print('Введите номер пункта меню от 1 до 7: ', end='')
