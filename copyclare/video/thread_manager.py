import time

from datetime import datetime
from copyclare.common import AppSingleton
from copyclare.model import Attempt


class ThreadManager:
    def __init__(self):

        self.thread_count = 0
        self.finished_count = 0

    def add_thread(self, thread, is_camera=False):
        self.thread_count += 1
        thread.finished.connect(self.thread_finished)
        if is_camera:
            self.worker = thread.worker

    def thread_finished(self):
        self.finished_count += 1
        if self.finished_count >= self.thread_count:
            # if all threads finished
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            attempt = Attempt(
                None,
                dt_string,
                self.worker.num_of_repetitions,
                time.time() - self.worker.beginning,
                "",
                self.worker.accuracy,
                self.worker.exercise.id,
            )

            AppSingleton.get_app().end_exercise(attempt)
