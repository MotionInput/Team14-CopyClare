"""
Contributors: Adi Bozzhanov, Yan Lai

"""

from copyclare.pyui.progress_chart_graph import Ui_Frame
from copyclare import UiElement


class ProgressChartGraphWidget(UiElement):
    def __init__(self, master):
        super().__init__(master, "progress_chart_graph", Ui_Frame)
