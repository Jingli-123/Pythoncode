import Backend
import Frontend
import sys

class Application:
    def __init__(self) -> None:
        self.__backend=Backend.CarRentalManager()
        self.__backend.data_file="data.csv"
        self.__frontend=Frontend.CarRentalManagerUI(self.__backend)
        sys.stdout.write("About to start program...")
        self.__frontend.show_ui()
app=Application()