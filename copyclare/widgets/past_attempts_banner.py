from PySide6.QtWidgets import QFileDialog

from copyclare.common import AppSingleton
from copyclare.data.exporter import Exporter
from copyclare.pyui.past_attempts_banner import Ui_Frame
from copyclare import UiElement


class PastAttemptsBannerWidget(UiElement):
    def __init__(self, master):
        super().__init__(master, "past_attempts_banner", Ui_Frame)
        self.app = AppSingleton.get_app()

        self.ui.export_all_button.clicked.connect(lambda x: self._export_all())

    # TODO - link export_all function here
    def _export_all(self):
        exporter = Exporter(self.app.db)
        file_path, selectedFilter = QFileDialog.getSaveFileName(
            filter="*.docx")
        exporter.export(file_path.strip(
        )+".docx" if "." not in file_path else file_path.strip())
