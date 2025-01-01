from PyQt5.QtWidgets import QMainWindow, QWidget
from Widgets import Widgets
from PyQt5.QtGui import QColor
from Layouts.Start_Layout import Start_Layout
from Layouts.New_Tournament_Layout import New_Tournament_Layout
from Layouts.Continue_Tournament_Layout import Continue_Tournament_Layout
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

    def resizeEvent(self,event):
        self.layout.resize(self.width(),self.height())

    def get_text(self, key):
        return self.app.text(key)
    
    def change_language(self, language):
        self.app.change_language(language)

    def delete_later(self):
        self.Central_widget.deleteLater()
        self.Central_widget = QWidget(self) 

    def new_tournament(self):
        self.delete_later()
        self.layout = New_Tournament_Layout(self)
        self.set_widget()
        self.show()

    def continue_tournament(self):
        self.delete_later()
        self.layout = Continue_Tournament_Layout(self)
        self.set_widget()
        self.show()