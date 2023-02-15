import json

from view import View
from note import Note


class JSONmodel(object):
    def __init__(self, filename):
        self.filename = filename
        self.notes = list()

    def create_note(self, note):
        self.notes = self.read_notes()
        max_id = 0
        for field in self.notes:
            if field.note_id > max_id:
                max_id = field.note_id
        note_id = max_id + 1
        note.note_id = note_id

        self.notes.append(note)
        self.write_json_file(self.notes)

    def read_notes(self):
        return self.read_json_file()

    def read_note(self, search_id):
        self.notes = self.read_notes()
        for note in self.notes:
            if note.note_id == search_id:
                return note
        else:
            View.print_note_id_not_exist(search_id)

    def update_note(self, search_id, note):
        self.notes = self.read_notes()
        for field in self.notes:
            if field.note_id == search_id:
                field.date = note.date
                field.title = note.title
                field.text = note.text

        self.write_json_file(self.notes)

    def delete_all_notes(self):
        self.notes = self.read_notes()
        self.notes.clear()
        self.write_json_file(self.notes)

    def write_json_file(self, notes):
        json_strings_list = list()
        for note in notes:
            json_strings_list.append({'id': note.note_id, 'date': note.date, 'title': note.title, 'text': note.text})

        notes_json = json.dumps(json_strings_list, indent=4, sort_keys=False, default=str)

        with open(self.filename, "w", encoding='utf-8') as my_file:
            my_file.write(notes_json)

    def read_json_file(self):
        notes_list = list()
        try:
            with open(self.filename, "r", encoding='utf-8') as my_file:
                notes_json = my_file.read()
            data = json.loads(notes_json)
            data.sort(key=lambda x: x['date'])
            for field in data:
                notes_list.append(Note(field['id'], field['date'], field['title'], field['text']))

            return notes_list
        except ValueError:
            return self.notes
