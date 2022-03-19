from .page import Page

from copyclare.common import AppSingleton

class AnalysisPage(Page):
    def __init__(self, master, attempt):
        super().__init__(master, "analysis")

        self.app = AppSingleton.get_app()
        name, desc = self.app.db.get_exercise_name_and_desc_by_ID(attempt.exercise_id)

        self.ui.name.setText(name)
        self.ui.description.setText(desc)
        self.ui.date.setText(attempt.date)
        self.ui.repetitions.setText(str(attempt.num_of_repetitons))
        self.ui.accuracy.setText(str(attempt.accuracy))

        # TODO things to set for QGraphicsView
        # heatmap, accuracy_graph

        self.ui.back_button.clicked.connect(lambda x: self.app.load_page("progress"))
