from docx import Document


class Exporter():
    def __init__(self, database):
        self.database = database
        self.doc = DocumentWriter()

    def export(self, saveAs, attempt_id=None):
        exercise_info = []
        quantitative_data = []
        qualitative_data = []
        export_title = ""
        if attempt_id is None:
            export_title = "Results for all attempts"
            attempts = self.database.get_all_attempts()
            for attempt in attempts:
                self.get_data(attempt, quantitative_data, qualitative_data)
        else:
            export_title = "Results for attempt %s" % attempt_id
            attempt = self.database.get_one_attempt_by_ID(attempt_id)
            self.get_data(attempt, exercise_info, quantitative_data,
                          qualitative_data)
        self.doc.create_document(saveAs, export_title, exercise_info,
                                 quantitative_data, qualitative_data)

    def get_data(self, attempt, exercise_info, quantitative_data,
                 qualitative_data):
        exe_id = attempt.exercise_id
        exe = self.database.get_one_exercise_by_ID(exe_id)
        exercise_info.append({
            "name": exe.name,
            "image": exe.image_directory,
            "description": exe.description
        })
        quantitative_data.append({
            "reps": attempt.num_of_repetitons,
            "duration": attempt.duration,
        })
        qualitative_data.append({
            "accuracy": attempt.accuracy,
        })


# reference: https://roytuts.com/a-guide-to-write-word-file-using-python/


class DocumentWriter():
    def __init__(self):
        self.document = Document()

    def create_document(self, saveAs, export_title, exercise_info,
                        quantitative_data, qualitative_data):
        self.document.add_heading(export_title, 0)
        self.add_name_and_description(exercise_info)
        self.add_quantitative_section(quantitative_data)
        self.add_qualitative_section(qualitative_data)
        self.document.save(saveAs)

    def add_name_and_description(self, exercise_info):
        for exercise in exercise_info:
            self.document.add_heading('Exercise Name: %s' % exercise["name"],
                                      level=2)
            # self.document.add_picture(
            #     exercise["image"])
            self.document.add_paragraph('Descripiton:  %s' %
                                        exercise["description"])

# which different exercises they performed
# number of repetition, time take

    def add_quantitative_section(self, quantitative_data):
        self.document.add_heading('Quantitative', level=2)
        table = self.document.add_table(rows=1, cols=2)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Repetitions'
        hdr_cells[1].text = 'Duration'
        for item in quantitative_data:
            row_cells = table.add_row().cells
            row_cells[0].text = str(item['reps'])
            row_cells[1].text = str(item['duration'])


# What we would ideally like to see is information
# about the person as they made the movement,
# and how that movement matched against the
# normal movement/reference movement.
# Ideally, we would like to get whole limb through
# range read out(Basically, how much they deviated
# from the normal range). For this we would want whole
# limb through range data in relation to the reference movement.

    def add_qualitative_section(self, qualitative_data):
        self.document.add_heading('Qualitative', level=2)
        table = self.document.add_table(rows=1, cols=1)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Accuracy'
        print("this is qualitative data", qualitative_data)
        for item in qualitative_data:
            row_cells = table.add_row().cells
            row_cells[0].text = str(item['accuracy'])
