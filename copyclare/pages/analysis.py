"""
AnalysisPage`


"""
from copyclare.pyui.analysis import Ui_analysis_page
from copyclare.common import AppSingleton
from copyclare import UiElement


class AnalysisPage(UiElement):
    def __init__(self, master, attempt):
        super().__init__(master, "analysis", Ui_analysis_page)

        self.app = AppSingleton.get_app()
        name, desc = self.app.db.get_exercise_name_and_desc_by_ID(
            attempt.exercise_id)

        self.ui.name.setText(name)
        self.ui.description.setText(desc)
        self.ui.date.setText(attempt.date)
        self.ui.repetitions.setText(str(attempt.num_of_repetitons))
        self.ui.accuracy.setText(str(attempt.accuracy))

        self.ui.back_button.clicked.connect(
            lambda x: self.app.load_page("progress"))
