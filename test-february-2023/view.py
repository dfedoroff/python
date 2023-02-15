class View(object):

    @staticmethod
    def print_saved_note(note):
        print(note)

    @staticmethod
    def print_all_saved_notes(notes):
        for note in notes:
            print(note)

    @staticmethod
    def print_notes_not_exist():
        print('\nСписок заметок пуст')

    @staticmethod
    def print_note_id_exist(note_id):
        print('\nЗаметка с id: {} уже есть'.format(note_id))
