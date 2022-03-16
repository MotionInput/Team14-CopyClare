from database import Database
from docx import Document
from docx.shared import Inches


class Exporter():
    def __init__(self):
        self.database = Database.main()

    def export_all(self):
        attempts = self.database.get_all_attempts()
        for attempt in attempts:
            exe_id = attempt.exercise_id
            exe = self.database.get_one_exercise_by_ID(exe_id)
            exe_name = exe.name
            exe_des = exe.description
            print(exe_id, exe_name, exe_des)

    def export(self, exe_id):
        exe = self.database.get_one_exercise_by_ID(exe_id)
        exe_name = exe.name
        exe_des = exe.description
        print(exe_id, exe_name, exe_des)



class DocumentWriter():
    def __init__(self):
        self.document = Document()

    def create_document(self):
        self.document.add_heading('Results', 0)
        self.add_quantitative_section()
        self.add_qualitative_section()

# which different exercises they performed, number of sets,
# number of repetition, time take, Number of time
# they get to the range required.
    def add_quantitative_section(self):
        self.document.add_heading('Quantitative', level=1)

    def add_qualitative_section(self):
        self.document.add_heading('Qualitative', level=1)
