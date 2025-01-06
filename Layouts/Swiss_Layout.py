from PyQt5.QtWidgets import QLineEdit,QPushButton,QGridLayout,QWidget,QFileDialog,QMessageBox
from PyQt5.QtGui import QIntValidator


class Swiss_Layout(QGridLayout):


    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        pass