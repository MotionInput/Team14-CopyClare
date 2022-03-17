from .page import Page

from copyclare.model import database

class AnalysisPage(Page):
    def __init__(self, master, attempt):
        super().__init__(master, "analysis")

        data = database.main()
        name, desc = data.get_exercise_name_and_desc_by_ID(attempt.exercise_id)

        self.ui.name.setText(name)
        self.ui.description.setText(desc)
        self.ui.date.setText(attempt.date)
        self.ui.repetitions.setText(attempt.num_of_repetitons)
        self.ui.accuracy.setText(attempt.accuracy)

        # TODO things to set for QGraphicsView
        # heatmap, accuracy_graph
        # TODO back_button
