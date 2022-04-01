"""
Contributors: Adi Bozzhanov, Yan Lai, Sree Sanakkayala

"""

import json
import time
from datetime import datetime

from copyclare.common import AppSingleton
from copyclare.data.objects import Attempt


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

        self.finished_count += 1
        if self.finished_count >= self.thread_count:
            # if all threads finished
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            avg = 0
            for t, each in self.worker.accuracy_vals:
                avg += each
            if len(self.worker.accuracy_vals) != 0:
                avg /= len(self.worker.accuracy_vals)

            attempt = Attempt(
                None,
                dt_string,
                self.worker.num_of_repetitions,
                round(time.time() - self.worker.beginning, 2),
                json.dumps(self.worker.accuracy_vals, indent=4),
                round(avg, 2),
                self.worker.exercise.id,
            )

            AppSingleton.get_app().end_exercise(attempt)
