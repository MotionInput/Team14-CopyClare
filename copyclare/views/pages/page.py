from PySide6.QtWidgets import QFrame

class Page(QFrame):

    def __init__(self, master, page_ui):

        super().__init__(master)
        self.ui = page_ui()
        self.ui.setupUi(self)

        

        
