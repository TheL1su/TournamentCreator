from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt

import copy


class Swiss_Result_layout(QVBoxLayout):


    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        #########################################################
        # Przyciski nastepna runda, zapisz i wyjdz
        self.Next_Round = self.main_window.create_push_button("Next_Round")
        self.Next_Round.clicked.connect(self.start_next_round)
        self.Save_And_Exit = self.main_window.create_push_button("Save_And_Exit")
        self.Save_And_Exit.clicked.connect(self.main_window.save_exit)

        

        #########################################################
        # layout wynikow
        #########################################################
        # wyczysc layout
        self.main_window.clear_layout(self)
        Layout = QVBoxLayout()
        players_data = self.main_window.get_players()
        
        ranking = self.main_window.create_bold_label("Ranking")
        Layout.addWidget(ranking)

        Legend = QHBoxLayout()
        Players = self.main_window.create_bold_label("Player")
        Big_points = self.main_window.create_bold_label("Big_Points")
        Small_points = self.main_window.create_bold_label("Small_Points")
        Legend.addWidget(Players)
        Legend.addWidget(Big_points)
        Legend.addWidget(Small_points)
        Legend.setAlignment(Big_points, Qt.AlignCenter)
        Legend.setAlignment(Small_points, Qt.AlignCenter)
        Layout.addLayout(Legend)

        for i, player in enumerate(players_data):
            Layout_Players = QHBoxLayout()

            player_label = self.main_window.create_player_label(player.get("name"),i+1)
            big = self.main_window.create_num_label(player.get("big_points"))
            small = self.main_window.create_num_label(player.get("small_points"))

            Layout_Players.addWidget(player_label)
            Layout_Players.addWidget(big)
            Layout_Players.addWidget(small)
            Layout_Players.setAlignment(big, Qt.AlignCenter)
            Layout_Players.setAlignment(small, Qt.AlignCenter)
            Layout.addLayout(Layout_Players)
            
        self.addLayout(Layout)
        Layout_Buttons = QHBoxLayout()
        Layout_Buttons.addWidget(self.Next_Round)
        Layout_Buttons.addWidget(self.Save_And_Exit)
        self.addLayout(Layout_Buttons)
        # self.show()


    def start_next_round(self):
        self.main_window.start_new_round()

    def resize(self,width,height):
        """zmiana wielkosci przyciskow przy zmianie rozmiaru okna CT"""
        pass
