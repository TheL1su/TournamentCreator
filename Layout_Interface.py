from abc import abstractmethod
from PyQt5.QtWidgets import QGridLayout

class Layout_Interface(QGridLayout):

    @abstractmethod
    def resize(self):
        pass