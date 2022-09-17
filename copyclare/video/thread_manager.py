"""
Contributors: Adi Bozzhanov, Yan Lai, Sree Sanakkayala

"""

import json
import time
from datetime import datetime

from copyclare.common import AppSingleton
from copyclare.data.database import Attempt, AttemptData


class ThreadManager:
    """
    Manages video and camera threads that are run
    on the exercise page

    """
    def __init__(self):

        self.thread_count = 0
        self.finished_count = 0

    def add_thread(self, thread, is_camera=False):
        """
        Adds a thread to the list of considered
        threads
        """

        self.thread_count += 1
        thread.finished.connect(self.thread_finished)
        if is_camera:
            self.worker = thread.worker

    def thread_finished(self):
        """
        Makes sure that both threads are finished
        before an attempt intance is created in the db
        """
        self.app = AppSingleton.get_app()
        self.finished_count += 1
        if self.finished_count >= self.thread_count:
            # if all threads finished
            now = datetime.now()
            avg = 0
            for _, each in self.worker.accuracy_vals:
                avg += each
            if len(self.worker.accuracy_vals) != 0:
                avg /= len(self.worker.accuracy_vals)
            attempt = Attempt(
                exercise=self.worker.exercise,
                datetime=now,
                reps=len(self.worker.accuracy_vals),
                average_accuracy=avg,
                duration=time.time() - self.worker.beginning
            )

            for t, each in self.worker.accuracy_vals:
                attempt.data.append(AttemptData(time=t, accuracy=each))

            AppSingleton.get_app().end_exercise(attempt)
