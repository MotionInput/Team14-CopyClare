from copyclare.common import AppSingleton

if __name__ == "__main__":

    app = AppSingleton.get_app()
    app.start_ui()
