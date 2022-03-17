from copyclare.common import AppSingleton


class ThreadManager:
    def __init__(self):

        self.thread_count = 0
        self.finished_count = 0

    def add_thread(self, thread):
        self.thread_count += 1
        thread.finished.connect(self.thread_finished)

    def thread_finished(self):
        self.finished_count += 1
        if self.finished_count >= self.thread_count:
            # if all threads finished
            AppSingleton.get_app().end_exercise()
