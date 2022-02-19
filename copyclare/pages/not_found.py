from .page import Page


class NotFound(Page):
    def __init__(self, master):
        super().__init__(master, "not_found")
