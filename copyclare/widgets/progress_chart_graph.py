from PySide6.QtWidgets import QFrame

from copyclare.common import load_ui


class ProgressChartGraphWidget(QFrame):
    def __init__(self, master):
        super().__init__(master)
        self.ui = load_ui("progress_chart_graph")
        self.ui.setupUi(self)
