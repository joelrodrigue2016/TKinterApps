from PyQt5.QtWidgets import *
from PyQt5 import uic


class MyGui(QMainWindow):
    """Running the application"""

    def __init__(self):
        super(MyGui, self).__init__()
        uic.loadUi("Mygui.ui", self)
        self.show()


def main():
    """main method"""
    app = QApplication([])
    window = MyGui()
    app.exec_()

    """Running the application"""


if __name__ == "__main__":
    main()
