from PySide6.QtCore import Qt


from .page import Page

class Video_Addition(Page):
    def __init__(self, master):
        super().__init__(master, "ADD VIDEO")

        video_name = self.ui.video_name_editor.getText()
        video_description = self.ui.description_editor.getText()
        video_tags = self.ui.tags_editor.getText()

        self.ui.back_button.clicked.connect(lambda x: self.app.load_page("home"))

        
