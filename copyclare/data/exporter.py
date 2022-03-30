

"""

This export module deals with everything related to exporting progress reports for the users

.. code-block:: python

   # sample usage:
   from copyclare.data import Exporter

   # Exporter is an object that allows for the exporting of progress reports
"""

import os
import json
import pyqtgraph as pg

from pyqtgraph import exporters
from docx import Document
from docx.shared import Inches

from copyclare.data import DATA_DIR

DOCX_MAX_IMAGE_WIDTH = Inches(6.5)


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
                self._get_data(
                    attempt, exercise_info, quantitative_data, qualitative_data)
        else:
            export_title = "Results for attempt %s" % attempt_id
            attempt = self.database.get_one_attempt_by_ID(attempt_id)
            self._get_data(attempt, exercise_info, quantitative_data,
                           qualitative_data)
        self.doc.create_document(saveAs, export_title, exercise_info,
                                 quantitative_data, qualitative_data)

    def _get_data(self, attempt, exercise_info, quantitative_data,
                  qualitative_data):
        exe_id = attempt.exercise_id
        exe = self.database.get_one_exercise_by_ID(exe_id)
        exercise_info.append({
            "name": exe.name,
            "image": exe.image_directory,
            "description": exe.description,
            "id": exe.id,
        })
        quantitative_data.append({
            "reps": attempt.num_of_repetitons,
            "duration": round(attempt.duration, 2),
        })
        qualitative_data.append({
            "accuracy": round(attempt.accuracy, 2),
            "accuracy_graph": DATA_DIR+f"/accuracy-graphs/{attempt.id}.png",
        })


# reference: https://roytuts.com/a-guide-to-write-word-file-using-python/


class DocumentWriter():
    def __init__(self):
        self.document = Document()

    def create_document(self, saveAs, export_title, exercise_info,
                        quantitative_data, qualitative_data):
        self.document.add_heading(export_title, 0)
        self._add_all_progress_charts(exercise_info)
        for i in range(len(exercise_info)):
            self._add_name_and_description(exercise_info[i])
            self._add_quantitative_section(quantitative_data[i])
            self._add_qualitative_section(qualitative_data[i])
        self.document.save(saveAs)

    def _add_all_progress_charts(self, exercise_info):
        displayed_exercises = set()
        for exercise in exercise_info:
            if exercise["id"] not in displayed_exercises:
                self.document.add_heading('Progress Chart for %s over time' %
                                          exercise["name"], level=2)
                exe_id = exercise["id"]
                self.document.add_picture(
                    DATA_DIR+f"/progress-charts/{exe_id}.png", width=DOCX_MAX_IMAGE_WIDTH)
                displayed_exercises.add(exe_id)

    def _add_name_and_description(self, exercise_info):
        self.document.add_heading('Exercise Name: %s' % exercise_info["name"],
                                  level=2)
        # self.document.add_picture(
        #     exercise["image"])
        self.document.add_paragraph('Description:  %s' %
                                    exercise_info["description"])

    def _add_quantitative_section(self, quantitative_data):
        self.document.add_heading('Quantitative', level=2)
        table = self.document.add_table(rows=1, cols=2)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Repetitions'
        hdr_cells[1].text = 'Duration'
        row_cells = table.add_row().cells
        row_cells[0].text = str(quantitative_data['reps'])
        row_cells[1].text = str(quantitative_data['duration'])

    def _add_qualitative_section(self, qualitative_data):
        self.document.add_heading('Qualitative', level=2)
        table = self.document.add_table(rows=1, cols=1)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Accuracy'
        row_cells = table.add_row().cells
        row_cells[0].text = str(qualitative_data['accuracy'])
        self.document.add_heading('Accuracy graph for attempt', level=3)
        self.document.add_picture(
            qualitative_data["accuracy_graph"], width=DOCX_MAX_IMAGE_WIDTH)


class AccuracyGraphExporter:
    def draw_accuracy_graph(self, session_json):
        graphWidget = pg.PlotWidget()

        x_axis = []
        y_axis = []

        accuracy = json.loads(session_json)

        for pair in accuracy:
            x_axis.append(pair[0])  # timestamp
            y_axis.append(pair[1])  # accuracy

        graphWidget.setBackground('w')
        graphWidget.setTitle(
            "Accuracy throughout exercise (recorded by second)", color="black", size="15pt")
        graphWidget.showGrid(x=True, y=True)
        graphWidget.setXRange(x_axis[0], x_axis[-1], padding=0)
        graphWidget.setYRange(0, 100, padding=0)

        pen = pg.mkPen(color=(0, 20, 40), width=3)
        graphWidget.plot(x_axis, y_axis, name="",  pen=pen,
                         symbol='o', symbolSize=2, symbolBrush=('#003366'))

        return graphWidget

    def export_accuracy_graph(self, session_json, attempt_id):
        path = DATA_DIR + '/accuracy-graphs/' + str(attempt_id) + '.png'
        exists = os.path.exists(path)
        if not exists:
            accuracy_graph = self.draw_accuracy_graph(session_json)
            exporter = exporters.ImageExporter(accuracy_graph.plotItem)
            exporter.parameters()['width'] = 500
            exporter.parameters()['height'] = 400
            exporter.export(path)
