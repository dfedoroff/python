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

    @staticmethod
    def print_note_id_not_exist(note_id):
        print('\nЗаметки с id: {} нет'.format(note_id))

    @staticmethod
    def print_note_saved():
        print('\nНовая заметка сохранена')

    @staticmethod
    def print_note_updated(note_id):
        print('\nЗаметка с id:{} обновлена'
              .format(note_id))

    @staticmethod
    def print_note_deleted(note_id):
        print('\nЗаметка с id: {} удалена'.format(note_id))

    @staticmethod
    def print_all_notes_deleted():
        print('\nВсе заметки удалены')
