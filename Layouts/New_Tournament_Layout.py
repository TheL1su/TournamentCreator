#from Layouts.Layout_Interface import Layout_Interface
from PyQt5.QtWidgets import QGridLayout,QLineEdit,QPushButton,QMessageBox,QWidget,QMenu,QAction, QHBoxLayout, QListWidgetItem, QListWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QRegularExpression
from PyQt5.QtGui import QIntValidator, QRegularExpressionValidator

class New_Tournament_Layout(QHBoxLayout):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        #########################################################
        # Tablica informacji czy zostaly wprowadzone informacje:
        # 0 indeks - Min_at_table
        # 1 indeks - Max_at_table
        # 2 indeks - typ turnieju
        # 3 indeks - dodani gracze
        self.check_buttons = [False,False,False,False]
        #########################################################
        # Labele do Ustawien Turnieju 
        Label_Min_Players_at_Table = self.main_window.create_bold_label("Enter_Min_Players_At_Table")
        Label_Max_Players_at_Table = self.main_window.create_bold_label("Enter_Max_Players_At_Table")

        #########################################################
        # Przyciski do Ustawien Turnieju 
        self.Min_at_Table_number_input = self.main_window.create_line_edit()
        self.Min_at_Table_number_input.setFixedWidth(50)
        self.Max_at_Table_number_input = self.main_window.create_line_edit()
        self.Max_at_Table_number_input.setFixedWidth(50)

        #########################################################
        # Validator dla Min i Maks - wartosci od 1 do 20
        validator = QRegularExpressionValidator(QRegularExpression("([1-9]|[1][0-9]|[2][0])"))
        self.Min_at_Table_number_input.setValidator(validator)
        self.Max_at_Table_number_input.setValidator(validator)

        #########################################################
        # Menu Turnieju
        Tournament_Menu = QMenu(parent = self.main_window)
        self.Tournament_Swiss = QAction(self.main_window.get_text("Swiss"), self.main_window)
        self.Tournament_Single_Elimination = QAction(self.main_window.get_text("PlayOff"), self.main_window)
        self.Tournament_Swiss.triggered.connect(lambda: self.add_type("Swiss"))
        self.Tournament_Single_Elimination.triggered.connect(lambda: self.add_type("Single_Elimination"))
        Tournament_Menu.addAction(self.Tournament_Swiss)
        Tournament_Menu.addAction(self.Tournament_Single_Elimination)


        #########################################################
        # Przycisk do Rodzaju Turnieju
        self.Tournament_Type = self.main_window.create_tool_button("Choose_Tournament_Type",Tournament_Menu)
        # self.Tournament_Type.setFixedWidth(300)

        #########################################################
        # Przycisk do Rozpoczecia Turnieju
        self.Start_Tournament = self.main_window.create_push_button("Start_Tournament")
        self.Start_Tournament.clicked.connect(self.OpenTournament)
        #########################################################
        # Funkcje wywolywane przy nacisnieciu przyciskow zatwierdz
        self.Min_at_Table_number_input.returnPressed.connect(self.Min_on_submit)
        self.Max_at_Table_number_input.returnPressed.connect(self.Max_on_submit)


        ########################################################
        # Dodawanie uczestnika
        Label_Add_Player = self.main_window.create_bold_label("Enter_Player")
        self.Add_Player_input = self.main_window.create_line_edit()
        self.Add_Player_input.setFixedWidth(400)
        self.Add_Player_input.setValidator(QRegularExpressionValidator(QRegularExpression("^[A-Z]{1}[a-z]* [A-Z]{1}[a-z]*")))  # Przyjmuje dwa słowa wielką literą

        ########################################################
        # Dodawanie uczestnika
        self.List_of_players_widget = QListWidget()
        self.Add_Player_input.returnPressed.connect(self.Add_player)

        #########################################################
        # Siatka dla Labeli i Przyciskow
        Layout_NT_settings = QVBoxLayout()
        Layout_NT_settings.addStretch()

        #########################################################
        # Dodanie Przyciskow - Minimalna ilosc graczy przy stole do siatki
        Layout_NT_settings.addWidget(Label_Min_Players_at_Table)
        Layout_NT_settings.addSpacing(10)
        Layout_NT_settings.addWidget(self.Min_at_Table_number_input)

        Layout_NT_settings.addSpacing(50)
        #########################################################
        # Dodanie Przyciskow - Maksymalna ilosc graczy przy stole do siatki
        Layout_NT_settings.addWidget(Label_Max_Players_at_Table)
        Layout_NT_settings.addSpacing(10)
        Layout_NT_settings.addWidget(self.Max_at_Table_number_input)
        Layout_NT_settings.addSpacing(50)
        #########################################################
        # Dodanie Menu Turniejow do siatki
        Layout_NT_settings.addWidget(self.Tournament_Type)
        Layout_NT_settings.addSpacing(50)

        #########################################################
        # Dodawanie dodaj gracza do siatki
        Layout_NT_settings.addWidget(Label_Add_Player)
        Layout_NT_settings.addSpacing(10)
        Layout_NT_settings.addWidget(self.Add_Player_input)
        Layout_NT_settings.addSpacing(50)
        Layout_NT_settings.addWidget(self.Start_Tournament)
        #########################################################
        # Ustawienie przyciskow na siatce
        Layout_NT_settings.setAlignment(Label_Min_Players_at_Table, Qt.AlignCenter)
        Layout_NT_settings.setAlignment(self.Min_at_Table_number_input, Qt.AlignCenter)
        Layout_NT_settings.setAlignment(Label_Max_Players_at_Table, Qt.AlignCenter)
        Layout_NT_settings.setAlignment(self.Max_at_Table_number_input, Qt.AlignCenter)
        Layout_NT_settings.setAlignment(Label_Add_Player,Qt.AlignCenter)
        Layout_NT_settings.setAlignment(self.Add_Player_input,Qt.AlignCenter)
        Layout_NT_settings.setAlignment(self.Tournament_Type,Qt.AlignCenter)
        Layout_NT_settings.setAlignment(self.Start_Tournament,Qt.AlignCenter)
        Layout_NT_settings.addStretch()
        # Layout_NT_settings.setStretch(Layout_NT_settings.rowCount(), 1)
        # Layout_NT_settings.setColumnStretch(Layout_NT_settings.columnCount(), 1)

        #########################################################
        # main layout

        self.addSpacing(20)
        self.addLayout(Layout_NT_settings,1)
        self.addSpacing(20)
        self.addWidget(self.List_of_players_widget,1)

    # Funkcja do obslugi wpisywania minimalnej wartosci dla stolu
    def Min_on_submit(self):
        number = int(self.Min_at_Table_number_input.text())
        if number:
            # Wartosc minimalna wieksza niz maks
            if self.main_window.tournament_max_at_table() != -1 and number > self.main_window.tournament_max_at_table():
                self.main_window.show_warning(self.main_window.get_text("Error"), self.main_window.get_text("Min_Bigger_Than_Max"))
            # Ustawienie Wartosci min_at_table w slowniku
            else:
                # Wprowadzono wartosc
                self.check_buttons[0] = True
                self.main_window.tournament_set_min_at_table(number) #Ustawienie Wartosci min_at_table w slowniku
                self.main_window.show_information(self.main_window.get_text("Value"), self.main_window.get_text("Value_Set") + str(number))
        else:
            #brak wpisanej wartosci
            self.main_window.show_warning(self.main_window.get_text("Error"), self.main_window.get_text("Value_Not_Set"))

# Funkcja do obslugi wpisywania maksymalnej wartosci dla stolu
    def Max_on_submit(self):
        number = int(self.Max_at_Table_number_input.text())
        if number:
            # Wartosc maksymalna mniejsza niz minimum
            if self.main_window.tournament_min_at_table() != -1 and number < self.main_window.tournament_min_at_table():
                self.main_window.show_warning(self.main_window.get_text("Error"), self.main_window.get_text("Max_Lower_Than_Min"))
            else:
                #Ustawienie Wartosci max_at_table w slowniku
                self.check_buttons[1] = True
                self.main_window.tournament_set_max_at_table(number)
                self.main_window.show_information(self.main_window.get_text("Value"), self.main_window.get_text("Value_Set") + str(number))
        else:
            #brak wpisanej wartosci
            self.main_window.show_warning(self.main_window.get_text("Error"), self.main_window.get_text("Value_Not_Set"))


    # #####################################################
    # # Metoda dodaje gracza i wypisuje go w liście
    def Add_player(self):
        if(self.check_buttons[3] is False): self.check_buttons[3] = True
        QListWidgetItem(self.Add_Player_input.text() , self.List_of_players_widget)
        self.main_window.tournament_add_player(self.Add_Player_input.text())
        self.Add_Player_input.clear()
 
    # #####################################################
    # # Metoda ustawia tryb turnieju
    def add_type(self, tournament_type):
        self.check_buttons[2] = True
        self.main_window.tournament_add_type(tournament_type)

    def resize(self,width,height):
        pass


    # #####################################################
    # funkcja odpalajaca turniej
    def OpenTournament(self):
        if(all(self.check_buttons)):
            self.main_window.open_tournament(new=True)
        else:
            self.main_window.show_warning(self.main_window.get_text("Error"),self.main_window.get_text("Not_All_Values_Set"))