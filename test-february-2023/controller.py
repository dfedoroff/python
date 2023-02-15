class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def print_all_notes(self):
        notes = self.model.read_notes()
        self.view.print_all_saved_notes(notes)
