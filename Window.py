from PyQt5.QtWidgets import QMainWindow, QWidget
from Widgets import Widgets
from PyQt5.QtGui import QColor
from Start_Layout import Start_Layout

class Window(QMainWindow):
    def __init__(self, app):
        self.app = app
        super().__init__()
        #########################################################
        #default Geometria
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle(self.app.text("Title"))
        self.widgetsStyle = Widgets()

        #########################################################
        # Kolor tla
        Color = self.palette()
        Color.setColor(self.backgroundRole(), QColor(41,44,51))
        self.setPalette(Color)

        #########################################################
        # Layout startowy
        self.layout = Start_Layout(self)

        self.Central_widget = QWidget(self)
        self.set_widget()
        self.show()

    def set_title(self):
        self.setWindowTitle(self.app.text("Title"))

    #########################################################
    # Ustawianie centralnego widgetu
    def set_widget(self):
        self.Central_widget.setLayout(self.layout)
        self.setCentralWidget(self.Central_widget)
        # self.initUI()

    def resizeEvent(self,event):
        self.layout.resize(self.width(),self.height())

    def get_text(self, key):
        return self.app.text(key)
    
    def change_language(self, language):
        self.app.change_language(language)

