from PySide6.QtWidgets import QFileDialog

from copyclare.common import AppSingleton
from copyclare.data.exporter import Exporter
"""
Contributors: Adi Bozzhanov, Yan Lai, Sree Sanakkayala

"""

from copyclare.pyui.past_attempts_banner import Ui_Frame
from copyclare import UiElement


class PastAttemptsBannerWidget(UiElement):
    def __init__(self, master):
        super().__init__(master, "past_attempts_banner", Ui_Frame)
        self.app = AppSingleton.get_app()

        self.ui.export_all_button.clicked.connect(lambda x: self._export_all())

    def _export_all(self):
        exporter = Exporter(self.app.db)
        file_path, selectedFilter = QFileDialog.getSaveFileName(
            filter="*.docx")
        exporter.export(file_path.strip(
        )+".docx" if "." not in file_path else file_path.strip())
