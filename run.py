from copyclare import App
from copyclare.common import AppSingleton

if __name__ == "__main__":

    app = App()
    app.shtuff = 123

    b = AppSingleton.get_app()
    print(b.shtuff)


    
