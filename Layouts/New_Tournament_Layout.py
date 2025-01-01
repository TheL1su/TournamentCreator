#from Layouts.Layout_Interface import Layout_Interface
from PyQt5.QtWidgets import QGridLayout,QLineEdit,QPushButton,QMessageBox,QWidget,QMenu,QAction, QHBoxLayout, QListWidgetItem, QListWidget
from PyQt5.QtCore import Qt, QRegularExpression
from PyQt5.QtGui import QIntValidator, QRegularExpressionValidator

class New_Tournament_Layout(QHBoxLayout):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        #########################################################
        # Labele do Ustawien Turnieju 
        Label_Min_Players_at_Table = self.main_window.widgetsStyle.create_label(self.main_window.get_text("Enter_Min_Players_At_Table"))
        Label_Max_Players_at_Table = self.main_window.widgetsStyle.create_label(self.main_window.get_text("Enter_Max_Players_At_Table"))

        #########################################################
        # Przyciski do Ustawien Turnieju 
        self.Min_at_Table_number_input = QLineEdit()
        self.Min_at_Table_number_input.setFixedWidth(300)
        self.Max_at_Table_number_input = QLineEdit()
        self.Max_at_Table_number_input.setFixedWidth(300)
        self.Min_at_Table_number_input.setValidator(QIntValidator(1,20))  # Przyjmuje tylko liczby całkowite
        self.Max_at_Table_number_input.setValidator(QIntValidator(1,20))  # Przyjmuje tylko liczby całkowite
        self.Min_submit_button = QPushButton(self.main_window.get_text("Submit"))
        self.Max_submit_button = QPushButton(self.main_window.get_text("Submit"))

        #########################################################
        # Menu Turnieju
        Tournament_Menu = QMenu(parent = self.main_window)
        self.Tournament_Swiss = QAction("System Szwajcarski", self.main_window)
        self.Tournament_Brasil = QAction("System Brazylijski", self.main_window)
        Tournament_Menu.addAction(self.Tournament_Swiss)
        Tournament_Menu.addAction(self.Tournament_Brasil)


        #########################################################
        # Przycisk do Rodzaju Turnieju
        self.Tournament_Type = self.main_window.widgetsStyle.create_tool_button(parent=self.main_window, text=self.main_window.get_text("Choose_Tournament_Type"), menu=Tournament_Menu)
        self.Tournament_Type.setFixedSize(300,20)

        #########################################################
        # Funkcje wywolywane przy nacisnieciu przyciskow zatwierdz
        self.Min_submit_button.clicked.connect(self.Min_on_submit)
        self.Max_submit_button.clicked.connect(self.Max_on_submit)


        ########################################################
        # Dodawanie uczestnika
        Label_Add_Player = self.main_window.widgetsStyle.create_label(self.main_window.get_text("Enter_Player"))
        self.Add_Player_input = QLineEdit()
        self.Add_Player_input.setFixedWidth(300)
        self.Add_Player_input.setValidator(QRegularExpressionValidator(QRegularExpression("^[A-Z]{1}[a-z]* [A-Z]{1}[a-z]*")))  # Przyjmuje dwa słowa wielką literą
        self.Add_Player_button = QPushButton(self.main_window.get_text("Submit"))

        ########################################################
        # Dodawanie uczestnika
        self.List_of_players_widget = QListWidget()
        self.Add_Player_button.clicked.connect(self.Add_player)

        #########################################################
        # Siatka dla Labeli i Przyciskow
        Layout_NT_settings = QGridLayout()

        #########################################################
        # Dodanie Przyciskow - Minimalna ilosc graczy przy stole do siatki
        Layout_NT_settings.addWidget(Label_Min_Players_at_Table,0,0)
        Layout_NT_settings.addWidget(self.Min_at_Table_number_input,1,0)
        Layout_NT_settings.addWidget(self.Min_submit_button,1,1)

        #########################################################
        # Dodanie Przyciskow - Maksymalna ilosc graczy przy stole do siatki
        Layout_NT_settings.addWidget(Label_Max_Players_at_Table,2,0)
        Layout_NT_settings.addWidget(self.Max_at_Table_number_input,3,0)
        Layout_NT_settings.addWidget(self.Max_submit_button,3,1)
        
        #########################################################
        # Dodanie Menu Turniejow do siatki
        Layout_NT_settings.addWidget(self.Tournament_Type,4,0)

        #########################################################
        # Dodawanie dodaj gracza do siatki
        Layout_NT_settings.addWidget(Label_Add_Player,5,0)
        Layout_NT_settings.addWidget(self.Add_Player_input,6,0)
        Layout_NT_settings.addWidget(self.Add_Player_button,6,1)

        #########################################################
        # Ustawienie przyciskow na siatce
        Layout_NT_settings.setAlignment(Label_Min_Players_at_Table, Qt.AlignLeft)
        Layout_NT_settings.setAlignment(self.Min_at_Table_number_input, Qt.AlignLeft)
        Layout_NT_settings.setAlignment(self.Min_submit_button,Qt.AlignCenter)
        Layout_NT_settings.setAlignment(Label_Max_Players_at_Table, Qt.AlignLeft)
        Layout_NT_settings.setAlignment(self.Max_at_Table_number_input, Qt.AlignLeft)
        Layout_NT_settings.setAlignment(self.Max_submit_button,Qt.AlignCenter)
        Layout_NT_settings.setAlignment(self.Tournament_Type,Qt.AlignCenter)
        Layout_NT_settings.setRowStretch(Layout_NT_settings.rowCount(), 1)
        Layout_NT_settings.setColumnStretch(Layout_NT_settings.columnCount(), 1)

        #########################################################
        # main layout

        self.addLayout(Layout_NT_settings)
        self.addWidget(self.List_of_players_widget)


# Funkcja do obslugi wpisywania minimalnej wartosci dla stolu
    def Min_on_submit(self):
        number = self.Min_at_Table_number_input.text()
        if number:
            # Wartosc minimalna wieksza niz maks
            if "Max_at_table" in self.TournamentDict and number > self.TournamentDict.get("Max_at_table"):
                QMessageBox.warning(self, self.main_window.get_text("Error"), self.main_window.get_text("Min_Bigger_Than_Max"))
            # Ustawienie Wartosci min_at_table w slowniku
            else:
                self.TournamentDict.update({"Min_at_table": number}) #Ustawienie Wartosci min_at_table w slowniku
                QMessageBox.information(self, self.main_window.get_text("Value"), self.main_window.get_text("Value_Set") + number)
        else:
            #brak wpisanej wartosci
            QMessageBox.warning(self, self.main_window.get_text("Error"), self.main_window.get_text("Value_Not_Set"))

# Funkcja do obslugi wpisywania maksymalnej wartosci dla stolu
    def Max_on_submit(self):
        number = self.Max_at_Table_number_input.text()
        if number:
            # Wartosc maksymalna mniejsza niz minimum
            if "Min_at_table" in self.TournamentDict and number < self.TournamentDict.get("Min_at_table"):
                QMessageBox.warning(self, self.main_window.get_text("Error"), self.main_window.get_text("Max_Lower_Than_Min"))
            else:
                #Ustawienie Wartosci max_at_table w slowniku
                self.TournamentDict.update({"Max_at_table": number})
                QMessageBox.information(self, self.main_window.get_text("Value"), self.main_window.get_text("Value_Set") + number)
        else:
            #brak wpisanej wartosci
            QMessageBox.warning(self, self.main_window.get_text("Error"), self.main_window.get_text("Value_Not_Set"))


# #####################################################
# # Metoda dodaje gracza i wypisuje go w liście
    def Add_player(self):
        #QListWidgetItem(self.Add_Player_input.text() , self.List_of_players_widget)
        #self.Add_Player_input.clear()
        pass


# def resize_nt(self):
#     """zmiana wielkosci przyciskow przy zmianie rozmiaru okna NT"""
#     pass

    def resize(self,width,height):
        pass