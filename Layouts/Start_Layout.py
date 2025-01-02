#from Layouts.Layout_Interface import Layout_Interface
from PyQt5.QtWidgets import QGridLayout, QPushButton,QMenu,QAction,QToolButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Start_Layout(QGridLayout):



    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        #########################################################
        # Przycisk Jezyka 
        Language_Menu = QMenu(parent = self.main_window)
        self.Language_Polski = QAction("Polski", self.main_window)
        self.Language_English = QAction("English", self.main_window)
        Language_Menu.addAction(self.Language_Polski)
        Language_Menu.addAction(self.Language_English)

        self.Language_Choice = self.main_window.create_tool_button("Choose_Language",Language_Menu)

        #########################################################
        # Przycisk nowy i kontunuuj turniej
        self.New_Tournament = QPushButton(self.main_window.get_text("New_Tournament"), self.main_window)
        self.Continue_Tournament = QPushButton(self.main_window.get_text("Continue_Tournament"),self.main_window)
        
        #########################################################
        # Funkcje wywolywane przy nacisnieciu przycisku NewTournament i ContinueTournament
        self.New_Tournament.clicked.connect(self.main_window.new_tournament)
        self.Continue_Tournament.clicked.connect(self.main_window.continue_tournament)

        #########################################################
        # Siatka dla Przyciskow
        self.addWidget(self.Language_Choice,0,2)
        self.addWidget(self.New_Tournament,1,1)
        self.addWidget(self.Continue_Tournament,1,2)

        #########################################################
        # Ustawienie przyciskow na siatce
        self.setAlignment(self.New_Tournament, Qt.AlignTop | Qt.AlignCenter) #srodkowanie New_tournament
        self.setAlignment(self.Continue_Tournament,Qt.AlignTop | Qt.AlignCenter) #srodkowanie Continue_Tournament
        self.setAlignment(self.Language_Choice, Qt.AlignTop | Qt.AlignRight) #Ustawianie Language_Menu jezyka na prawo

        #########################################################
        # Zmiana jezyka aplikacji
        self.Language_Polski.triggered.connect(self.change_polish_language)
        self.Language_English.triggered.connect(self.change_english_language)




    # funkcja do zmiany jezyka aplikacji na polski
    def change_polish_language(self):
        self.main_window.change_language("polski")
        self.change_language()

    # funkcja do zmiany jezyka aplikacji na angielski
    def change_english_language(self):
        self.main_window.change_language("english")
        self.change_language()

    #funkcja zmieniajaca teksty przyciskow
    def change_language(self):
        self.main_window.set_title()
        self.New_Tournament.setText(self.main_window.get_text("New_Tournament"))
        self.Continue_Tournament.setText(self.main_window.get_text("Continue_Tournament"))
        self.Language_Choice.setText(self.main_window.get_text("Choose_Language"))
        self.main_window.show()



    def resize(self,width,height):
        """zmiana wielkosci przyciskow przy zmianie rozmiaru okna INIT"""
        font = QFont()
        font.setPointSize((width+height)//90) #ustawienie wielkosci czcionki
        self.Language_Choice.setFont(font)
        self.New_Tournament.setFont(font)
        self.Continue_Tournament.setFont(font)

        #Ustawienie wielkosci przyciskow
        self.Language_Choice.setFixedSize(width//5+50,height//10)
        self.New_Tournament.setFixedSize(width//4+60,height//10)
        self.Continue_Tournament.setFixedSize(width//4+60,height//10)