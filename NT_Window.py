from PyQt5.QtWidgets import QGridLayout,QLabel,QLineEdit,QPushButton,QMessageBox,QWidget,QToolButton,QMenu,QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator


def NewTournament_Window(self):
    #########################################################
    # Zmiana Trybu
    self.Mode = "NT"

    #########################################################
    # Slownik Turnieju
    self.TournamentDict = {}

    #########################################################
    # Labele do Ustawien Turnieju 
    Label_Min_Players_at_Table = QLabel(self.Language.Enter_Min_Players_At_Table())
    Label_Min_Players_at_Table.setStyleSheet('color: white;font-weight: bold')
    Label_Max_Players_at_Table = QLabel(self.Language.Enter_Max_Players_At_Table())
    Label_Max_Players_at_Table.setStyleSheet('color: white;font-weight: bold')

    #########################################################
    # Przyciski do Ustawien Turnieju 
    self.Min_at_Table_number_input = QLineEdit()
    self.Min_at_Table_number_input.setFixedWidth(300)
    self.Max_at_Table_number_input = QLineEdit()
    self.Max_at_Table_number_input.setFixedWidth(300)
    self.Min_at_Table_number_input.setValidator(QIntValidator(1,20))  # Przyjmuje tylko liczby całkowite
    self.Max_at_Table_number_input.setValidator(QIntValidator(1,20))  # Przyjmuje tylko liczby całkowite
    self.Min_submit_button = QPushButton(self.Language.Submit())
    self.Max_submit_button = QPushButton(self.Language.Submit())

    #########################################################
    # Menu Turnieju
    Tournament_Menu = QMenu(parent = self)
    self.Tournament_Swiss = QAction("System Szwajcarski", self)
    self.Tournament_Brasil = QAction("System Brazylijski", self)
    Tournament_Menu.addAction(self.Tournament_Swiss)
    Tournament_Menu.addAction(self.Tournament_Brasil)


    #########################################################
    # Przycisk do Rodzaju Turnieju
    self.Tournament_Type = QToolButton(parent = self)
    self.Tournament_Type.setText(self.Language.Choose_Tournament_Type())
    self.Tournament_Type.setMenu(Tournament_Menu)
    self.Tournament_Type.setPopupMode(QToolButton.InstantPopup)  # Ustawienie, aby Language_Menu rozwijało się natychmiast
    self.Tournament_Type.setStyleSheet("color: black;border-radius: 3px;background-color: rgb(0, 128, 255);font-family: Arial;")
    self.Tournament_Type.setFixedSize(300,20)
    #########################################################
    # Funkcje wywolywane przy nacisnieciu przyciskow zatwierdz
    self.Min_submit_button.clicked.connect(self.Min_on_submit)
    self.Max_submit_button.clicked.connect(self.Max_on_submit)

    #########################################################
    # Siatka dla Labeli i Przyciskow
    Layout_NT = QGridLayout()

    #########################################################
    # Dodanie Przyciskow - Minimalna ilosc graczy przy stole do siatki
    Layout_NT.addWidget(Label_Min_Players_at_Table,0,0)
    Layout_NT.addWidget(self.Min_at_Table_number_input,1,0)
    Layout_NT.addWidget(self.Min_submit_button,1,1)

    #########################################################
    # Dodanie Przyciskow - Maksymalna ilosc graczy przy stole do siatki
    Layout_NT.addWidget(Label_Max_Players_at_Table,2,0)
    Layout_NT.addWidget(self.Max_at_Table_number_input,3,0)
    Layout_NT.addWidget(self.Max_submit_button,3,1)
    
    #########################################################
    # Dodanie Menu Turniejow do siatki
    Layout_NT.addWidget(self.Tournament_Type,4,0)

    #########################################################
    # Ustawienie przyciskow na siatce
    Layout_NT.setAlignment(Label_Min_Players_at_Table, Qt.AlignLeft)
    Layout_NT.setAlignment(self.Min_at_Table_number_input, Qt.AlignLeft)
    Layout_NT.setAlignment(self.Min_submit_button,Qt.AlignCenter)
    Layout_NT.setAlignment(Label_Max_Players_at_Table, Qt.AlignLeft)
    Layout_NT.setAlignment(self.Max_at_Table_number_input, Qt.AlignLeft)
    Layout_NT.setAlignment(self.Max_submit_button,Qt.AlignCenter)
    Layout_NT.setAlignment(self.Tournament_Type,Qt.AlignCenter)
    Layout_NT.setRowStretch(Layout_NT.rowCount(), 1)
    Layout_NT.setColumnStretch(Layout_NT.columnCount(), 1)

    #########################################################
    # Usun stary i Wstaw nowy Widget Glowny
    self.Central_widget.deleteLater()
    self.Central_widget = QWidget(self)
    self.Central_widget.setLayout(Layout_NT)
    self.setCentralWidget(self.Central_widget)

    #########################################################
    # Wyswietlanie Okna
    self.show()

# Funkcja do obslugi wpisywania minimalnej wartosci dla stolu
def Min_on_submit(self):
    number = self.Min_at_Table_number_input.text()
    if number:
        # Wartosc minimalna wieksza niz maks
        if "Max_at_table" in self.TournamentDict and number > self.TournamentDict.get("Max_at_table"):
            QMessageBox.warning(self, self.Language.Error(), self.Language.Min_Bigger_Than_Max())
        # Ustawienie Wartosci min_at_table w slowniku
        else:
            self.TournamentDict.update({"Min_at_table": number}) #Ustawienie Wartosci min_at_table w slowniku
            QMessageBox.information(self, self.Language.Value(), self.Language.Value_Set() + number)
    else:
        #brak wpisanej wartosci
        QMessageBox.warning(self, self.Language.Error(), self.Languege.Value_Not_Set())

# Funkcja do obslugi wpisywania maksymalnej wartosci dla stolu
def Max_on_submit(self):
    number = self.Max_at_Table_number_input.text()
    if number:
        # Wartosc maksymalna mniejsza niz minimum
        if "Min_at_table" in self.TournamentDict and number < self.TournamentDict.get("Min_at_table"):
            QMessageBox.warning(self, self.Language.Error(), self.Language.Max_Lower_Than_Min())
        else:
            #Ustawienie Wartosci max_at_table w slowniku
            self.TournamentDict.update({"Max_at_table": number})
            QMessageBox.information(self, self.Language.Value(), self.Language.Value_Set() + number)
    else:
        #brak wpisanej wartosci
        QMessageBox.warning(self, self.Language.Error(), self.Languege.Value_Not_Set())

