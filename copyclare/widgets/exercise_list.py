from PySide6.QtWidgets import QFrame, QPushButton

from copyclare.common import load_ui


class ExerciseListWidget(QFrame):
    def __init__(self, master, exercises):
        super().__init__(master)

        self.ui = load_ui("exercise_list_widget")
        self.ui.setupUi(self)
        self.load_exercises(exercises)

    def load_exercises(self, exercises):
        # TODO: Replace with a database call

        for each in exercises:
            btn = QPushButton(self.ui.main_frame)
            btn.setText(each)

            name = Database.get_exercise()
            btn.clicked.connect(lambda x: print(f"hello {x}"))
            self.ui.main_layout.insertWidget(0, btn)
