from PySide6.QtWidgets import QFrame, QPushButton

from common import load_ui


class ExerciseListWidget(QFrame):
    def __init__(self, master):
        super().__init__(master)

        self.ui = load_ui("exercise_list_widget")
        self.ui.setupUi(self)
        self.load_exercises()

    def load_exercises(self):
        # TODO: Replace with a database call
        exercises = ["Shoulder Main", "Hand exercise 2", "Another Exercise"]

        for each in exercises:
            btn = QPushButton(self.ui.main_frame)
            btn.setText(each)
            btn.clicked.connect(lambda x: print(f"hello {x}"))
            self.ui.main_layout.insertWidget(0, btn)
