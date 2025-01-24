from PyQt5.QtWidgets import QLineEdit,QPushButton,QGridLayout,QWidget,QFileDialog,QMessageBox,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QIntValidator
import copy


class Swiss_Result_layout(QGridLayout):


    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        #########################################################
        # Przyciski nastepna runda, zapisz i wyjdz
        self.Next_Round = QPushButton(self.main_window.get_text("Next_Round"))
        self.Next_Round.clicked.connect(self.start_next_round)
        self.Save_And_Exit = QPushButton(self.main_window.get_text("Save_And_Exit"))
        self.Save_And_Exit.clicked.connect(self.main_window.save_exit)

        

        #########################################################
        # layout wynikow
        #########################################################
        # wyczysc layout
        self.main_window.clear_layout(self)
        Layout = QVBoxLayout()
        players_data = self.main_window.get_players()
        
        ranking = self.main_window.create_label("Ranking")
        Layout.addWidget(ranking)

        Legend = QHBoxLayout()
        Players = self.main_window.create_label("Player")
        Big_points = self.main_window.create_label("Big_Points")
        Small_points = self.main_window.create_label("Small_Points")
        Legend.addWidget(Players)
        Legend.addWidget(Big_points)
        Legend.addWidget(Small_points)
        Layout.addLayout(Legend)

        for i, player in enumerate(players_data):
            Layout_Players = QHBoxLayout()

            player_label = self.main_window.create_player_label(player.get("name"),i+1)
            big = self.main_window.create_num_label(player.get("big_points"))
            small = self.main_window.create_num_label(player.get("small_points"))

            Layout_Players.addWidget(player_label)
            Layout_Players.addWidget(big)
            Layout_Players.addWidget(small)

            Layout.addLayout(Layout_Players)
            
        self.addLayout(Layout,0,0)
        self.addWidget(self.Next_Round,1,0)
        self.addWidget(self.Save_And_Exit,1,1)
        # self.show()


    def start_next_round(self):
        self.main_window.start_new_round()

    def resize(self,width,height):
        """zmiana wielkosci przyciskow przy zmianie rozmiaru okna CT"""
        pass
    """
    #########################################################
    # Funkcja do sprawedzania czy wpisano ilosc rozgrywek w rundzie
    def Game_Num(self):
        number = self.Game_Num.text()
        if not number:
            QMessageBox.warning(self.main_window, self.main_window.get_text("Error"), self.main_window.get_text("Specify_Value_For_Round"))
    """