from copyclare.pyui.plan import Ui_planning
from copyclare.data.database import Plan

from copyclare import UiElement
from copyclare.common import AppSingleton


class PlanPage(UiElement):

    def __init__(self, master, exercise):
        super().__init__(master, "planning", Ui_planning)
        self.app = AppSingleton.get_app()

        self.exercise = exercise
        if exercise.plan is not None:
            self.ui.days_per_week_combo.setCurrentIndex(exercise.plan.days_per_week - 1)
            self.ui.sessions_per_day.setText(str(exercise.plan.sessions_per_day))
            self.ui.reps_per_session.setText(str(exercise.plan.reps_per_session))

        self.ui.cancel_button.clicked.connect(
            lambda x: self.app.load_page("home"))

        self.ui.submit_button.clicked.connect(self.confirm_plan)

    def confirm_plan(self):
        if self.exercise.plan is not None:
            plan = self.exercise.plan
        else:
            plan = Plan()
            self.exercise.plan = plan

        plan.days_per_week = int(self.ui.days_per_week_combo.currentText())
        plan.sessions_per_day = int(self.ui.sessions_per_day.text())
        plan.reps_per_session = int(self.ui.reps_per_session.text())
        self.app.db.session.commit()
        self.app.load_page("home")