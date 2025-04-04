from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton,QMenu,QAction,QToolButton
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt
from Language.Polski import Polski
from Language.English import English
from Widgets import Widgets

def initUI(self):
    #########################################################
    #default Jezyk i Geometria oraz tryb
    self.Language = Polski() #default Jezyk 
    self.setGeometry(100, 100, 400, 300)
    self.setWindowTitle(self.Language.Title())
    self.widgetsStyle = Widgets()
    self.Mode = "INIT"     

    #########################################################
    # Kolor tla
    Color = self.palette()
    Color.setColor(self.backgroundRole(), QColor(41,44,51))
    self.setPalette(Color)

    #########################################################
    # Slownik Turnieju
    self.TournamentDict = {}

    #########################################################
    # Przycisk Jezyka 
    Language_Menu = QMenu(parent = self)
    self.Language_Polski = QAction("Polski", self)
    self.Language_English = QAction("English", self)
    Language_Menu.addAction(self.Language_Polski)
    Language_Menu.addAction(self.Language_English)

    self.Language_Choice = self.widgetsStyle.create_tool_button(parent=self, text=self.Language.Choose_Language(), menu=Language_Menu)

    #########################################################
    # Przycisk nowy i kontunuuj turniej
    self.New_Tournament = QPushButton(self.Language.New_Tournament(), self)
    self.Continue_Tournament = QPushButton(self.Language.Continue_Tournament(),self)
    
    #########################################################
    # Funkcje wywolywane przy nacisnieciu przycisku NewTournament i ContinueTournament
    self.New_Tournament.clicked.connect(self.NewTournament_Window)
    self.Continue_Tournament.clicked.connect(self.ContinueTournament_Window)

    #########################################################
    # Siatka dla Przyciskow
    Layout = QGridLayout() 
    Layout.addWidget(self.Language_Choice,0,2)
    Layout.addWidget(self.New_Tournament,1,1)
    Layout.addWidget(self.Continue_Tournament,1,2)

    #########################################################
    # Ustawienie przyciskow na siatce
    Layout.setAlignment(self.New_Tournament, Qt.AlignTop | Qt.AlignCenter) #srodkowanie New_tournament
    Layout.setAlignment(self.Continue_Tournament,Qt.AlignTop | Qt.AlignCenter) #srodkowanie Continue_Tournament
    Layout.setAlignment(self.Language_Choice, Qt.AlignTop | Qt.AlignRight) #Ustawianie Language_Menu jezyka na prawo
    
    #########################################################
    # Widget Glowny
    self.Central_widget = QWidget(self)
    self.Central_widget.setLayout(Layout)
    self.setCentralWidget(self.Central_widget)

    #########################################################
    # Zmiana jezyka aplikacji
    self.Language_Polski.triggered.connect(self.change_polish_language)
    self.Language_English.triggered.connect(self.change_english_language)

    #########################################################
    # Wyswietlanie Okna
    self.show()


# funkcja do zmiany jezyka aplikacji na polski
def change_polish_language(self):
    self.Language = Polski()
    self.change_language()

# funkcja do zmiany jezyka aplikacji na angielski
def change_english_language(self):
    self.Language = English()
    self.change_language()

#funkcja zmieniajaca teksty przyciskow
def change_language(self):
    self.setWindowTitle(self.Language.Title())
    self.New_Tournament.setText(self.Language.New_Tournament())
    self.Continue_Tournament.setText(self.Language.Continue_Tournament())
    self.Language_Choice.setText(self.Language.Choose_Language())
    self.show()



def resize_init(self):
    """zmiana wielkosci przyciskow przy zmianie rozmiaru okna INIT"""
    font = QFont()
    font.setPointSize((self.width()+self.height())//90) #ustawienie wielkosci czcionki
    self.Language_Choice.setFont(font)
    self.New_Tournament.setFont(font)
    self.Continue_Tournament.setFont(font)

    #Ustawienie wielkosci przyciskow
    self.Language_Choice.setFixedSize(self.width()//5+50,self.height()//10)
    self.New_Tournament.setFixedSize(self.width()//4+60,self.height()//10)
    self.Continue_Tournament.setFixedSize(self.width()//4+60,self.height()//10)