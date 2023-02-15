import datetime
import ui
import re

from controller import Controller
from jsonmodel import JSONmodel
from note import Note
from view import View


def start():
    print('Вас приветствует приложение Заметки')
    controller = Controller(JSONmodel("notesdb.json"), View())

    while True:
        choice = ui.select_menu_item()

        if choice == 1:
            print('\nСоздать заметку:')
            controller.create_note(get_note_data())

        elif choice == 2:
            if controller.notes_exist():
                print('\nЧтобы прочитать заметку укажите её id: ', end='')
                note_id = get_int_input()
                if controller.note_id_exist(note_id):
                    controller.print_note(note_id)

        elif choice == 3:
            if controller.notes_exist():
                print('\nСписок сохраненных заметок:')
                controller.print_all_notes()

        elif choice == 4:
            if controller.notes_exist():
                print('\nЧтобы обновить заметку укажите её id: ', end='')
                note_id = get_int_input()
                if controller.note_id_exist(note_id):
                    controller.update_note(note_id, get_note_data())

        elif choice == 5:
            if controller.notes_exist():
                print('\nЧтобы удалить заметку укажите её id: ', end='')
                note_id = get_int_input()
                if controller.note_id_exist(note_id):
                    controller.delete_note(note_id)

        elif choice == 6:
            if controller.notes_exist():
                if input('\nУверены, что хотите удалить все заметки? [Да | Нет]: ').capitalize() == 'Да':
                    if controller.notes_exist():
                        controller.delete_all_notes()

        else:
            break


def get_int_input():
    while True:
        value = input()
        if re.match('^[1-9]\\d*$', value):
            return int(value)
        else:
            print('Введенное число не целое, отрицательное или равно нулю')
            print('Повторите ввод: ', end='')


def get_note_data():
    note_id = 0
    date = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    title = input('Заголовок заметки: ')
    text = input('Текст заметки: ')
    return Note(note_id, date, title, text)
