import json

from view import View
from note import Note


class JSONmodel(object):
    def __init__(self, filename):
        self.filename = filename
        self.notes = list()

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
