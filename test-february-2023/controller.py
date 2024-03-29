class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def print_all_notes(self):
        notes = self.model.read_notes()
        self.view.print_all_saved_notes(notes)

    def print_note(self, note_id):
        try:
            note = self.model.read_note(note_id)
            self.view.print_saved_note(note)
        except ValueError:
            self.view.print_note_id_not_exist(note_id)

    def create_note(self, note):
        self.model.create_note(note)
        self.view.print_note_saved()

    def update_note(self, note_id, note):
        self.model.update_note(note_id, note)
        self.view.print_note_updated(note_id)

    def delete_all_notes(self):
        self.model.delete_all_notes()
        self.view.print_all_notes_deleted()

    def delete_note(self, note_id):
        try:
            self.model.delete_note(note_id)
            self.view.print_note_deleted(note_id)
        except ValueError:
            self.view.print_note_id_not_exist(note_id)

    def notes_exist(self):
        notes = self.model.read_notes()
        if len(notes) == 0:
            self.view.print_notes_not_exist()
            return False
        else:
            return True

    def note_id_exist(self, search_id):
        notes = self.model.read_notes()
        for note in notes:
            if note.note_id == search_id:
                return True
        else:
            self.view.print_note_id_not_exist(search_id)
            return False

