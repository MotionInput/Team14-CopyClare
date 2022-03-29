from copyclare.common import AppSingleton

app = AppSingleton.get_app()
app.start_ui()
