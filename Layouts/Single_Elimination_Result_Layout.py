from PyQt5.QtWidgets import QLineEdit,QPushButton,QGridLayout,QWidget,QFileDialog,QMessageBox,QVBoxLayout,QHBoxLayout,QSizePolicy
from PyQt5.QtGui import QIntValidator
import copy

class Single_Elimination_Result_layout(QGridLayout):

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
        # Layout
        Layout_Tables = self.add_players_and_tables()

        self.addLayout(Layout_Tables,0,0)
        self.addWidget(self.Next_Round,1,0)
        self.addWidget(self.Save_And_Exit,1,1)

        # self.show()
        #self.addWidget(self.Save_And_Exit,1,1)


    def add_players_and_tables(self):
        #########################################################
        # Layout stolikow 
        Layout = QVBoxLayout()
        players = self.main_window.get_players()
        advancing_players = self.main_window.get_players("advancing_players")
        advancing_id = [player.get("id") for player in advancing_players]
        print("Players: ", players)
        print("Advancing_players:", advancing_players)

        
        #########################################################
        # ilos stolikow
        tables = self.main_window.get_tables()
        
        #########################################################
        # ilos graczy
        player_cnt = 0

        waitnig_label = self.main_window.create_bold_label("Waiting_Players")
        Layout.addWidget(waitnig_label)
        advancing_label = self.main_window.create_bold_label("Advancing")

        print([player.get("table") for player in players])

        while players[player_cnt].get("table")[0] == -1:
            player_label = self.main_window.create_player_label(players[player_cnt].get("name"),player_cnt+1,bold=True)
            player_label.setFixedWidth(100)
            player_label.setWordWrap(True)
            Layout.addWidget(player_label)
            player_cnt += 1

        print("player cnt: ",player_cnt)
        print("num of players:", len(players))

        # advancing_label = self.main_window.create_bold_label("Advancing")
        # eliminated_label = self.main_window.create_bold_label("Eliminated")

        
        for i in range(len(tables)):
            #########################################################
            # Label stolika
            table_number = self.main_window.create_table_label(i+1)
            Layout.addWidget(table_number)

            is_advancing = True
            advancing_label = self.main_window.create_bold_label("Advancing")
            eliminated_label = self.main_window.create_bold_label("Eliminated")
            Layout.addWidget(advancing_label)
            
            for j in range(tables[i]):
                #########################################################
                # layout gracza

                if is_advancing and players[player_cnt].get("id") not in advancing_id:
                    is_advancing = False
                    Layout.addWidget(eliminated_label)

                Layout_Players = QHBoxLayout()

                player_label = self.main_window.create_player_label(players[player_cnt].get("name"),j+1,bold=is_advancing)
                player_label.setFixedWidth(100)
                player_label.setWordWrap(True)
                Layout_Players.addWidget(player_label)

                Big_points = self.main_window.create_num_label(players[player_cnt].get("curr_big"))
                Big_points.setMaximumWidth(100)
                Small_points = self.main_window.create_num_label(players[player_cnt].get("curr_small"))
                Small_points.setMaximumWidth(100)
                
                Layout_Players.addWidget(Big_points)
                Layout_Players.addWidget(Small_points)
                
                player_cnt += 1

                Layout.addLayout(Layout_Players)

        return Layout


    def start_next_round(self):
        self.main_window.start_new_round()

    def resize(self,width,height):
        """zmiana wielkosci przyciskow przy zmianie rozmiaru okna CT"""
        pass
