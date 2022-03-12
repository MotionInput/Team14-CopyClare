from .page import Page

class AnalysisPage(Page):
    def __init__(self, master, attempt):
        super().__init__(master, "analysis")

        # TODO things to setText
        # name, description, date, repetitions, accuracy
        # TODO things to set for QGraphicsView
        # heatmap, accuracy_graph
        # TODO back_button
