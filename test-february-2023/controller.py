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
