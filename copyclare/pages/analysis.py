"""
AnalysisPage`


"""

from copyclare.data.exporter import AccuracyGraphExporter
from copyclare.pyui.analysis import Ui_analysis_page
from copyclare.common import AppSingleton
from copyclare import UiElement


class AnalysisPage(UiElement):
    def __init__(self, master, attempt):
        super().__init__(master, "analysis", Ui_analysis_page)
        self.attempt = attempt

        self.app = AppSingleton.get_app()
        name, desc = self.app.db.get_exercise_name_and_desc_by_ID(
            self.attempt.exercise_id)

        self.ui.name.setText(name)
        self.ui.description.setText(desc)
        self.ui.date.setText(self.attempt.date)
        self.ui.repetitions.setText(str(self.attempt.num_of_repetitons))
        self.ui.accuracy.setText(str(self.attempt.accuracy))

        self.accuracyGraphExporter = AccuracyGraphExporter()
        graphWidget = self.accuracyGraphExporter.draw_accuracy_graph(self.attempt.session_json)
        self.ui.verticalLayout_graph.addWidget(graphWidget)

        # TODO put exercise image here
        """img_path = DATA_DIR + f"/test/{exercise.id}.png"
        if os.path.exists(img_path):
            self.ui.ex_image.setPixmap(QPixmap(img_path))
        else:
            self.ui.ex_image.setPixmap(
                QPixmap(DATA_DIR + "/assets/default-video-img.png"))"""

        self.ui.back_button.clicked.connect(
            lambda x: self.app.load_page("progress"))
