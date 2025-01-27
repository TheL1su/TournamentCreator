from PyQt5.QtWidgets import QFileDialog,QMessageBox,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QRegularExpressionValidator
from PyQt5.QtCore import Qt, QRegularExpression



class Tournament_Layout(QVBoxLayout):


    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        #########################################################
        # Przyciski nastepna runda, zapisz i wyjdz
        self.Submit_Round = self.main_window.create_push_button("Submit_Round")
        self.Submit_Round.clicked.connect(self.filed_check)
        # self.Next_Round = QPushButton(self.main_window.get_text("Next_Round"))
        # self.Next_Round.clicked.connect(self.start_next_round)
        # self.Save_And_Exit = QPushButton(self.main_window.get_text("Save_And_Exit"))
        # self.Save_And_Exit.clicked.connect(self.save_exit)

        """
        #########################################################
        # Przyciski do wprowadzania ilosci rozgrywek w pojedynczej rundzie
        self.Game_Num = QLineEdit()
        self.Game_Num.setValidator(QIntValidator(1,20))
        self.Submit_Game_Num = QPushButton(self.main_window.get_text("Submit"))
        """
        
    def add_widgets(self):
        #########################################################
        # Layout
        Layout_Tables = self.add_players_and_tables()
        self.addStretch()
        self.addLayout(Layout_Tables)
        self.addStretch()
        self.addWidget(self.Submit_Round)

        # self.show()
        #self.addWidget(self.Save_And_Exit,1,1)


    def add_players_and_tables(self):
        #########################################################
        # Layout stolikow 
        Layout = QVBoxLayout()
        players = self.main_window.get_players()
        
        #########################################################
        # ilos stolikow
        tables = self.main_window.get_tables()
        
        #########################################################
        # ilos graczy
        player_cnt = 0

        if players[player_cnt].get("table")[0] == -1:
            waiting_label = self.main_window.create_label("Waiting_Players", bold=True)
            Layout.addWidget(waiting_label)


        while players[player_cnt].get("table")[0] == -1:
            player_label = self.main_window.create_player_label(players[player_cnt].get("name"),player_cnt+1)
            player_label.setFixedWidth(100)
            player_label.setWordWrap(True)
            Layout.addWidget(player_label)
            player_cnt += 1

        Layout.addSpacing(20)

        for i in range(len(tables)):
            
            #########################################################
            # Label stolika, duzych i malych punktow
            Layout_info = QHBoxLayout()
            table_number = self.main_window.create_table_label(i+1)
            big_points_info = self.main_window.create_bold_label("Big_Points")
            small_points_info = self.main_window.create_bold_label("Small_Points")
            
            Layout_info.addWidget(table_number)
            Layout_info.addWidget(big_points_info)
            Layout_info.addWidget(small_points_info)

            Layout_info.setAlignment(table_number, Qt.AlignLeft)
            Layout_info.setAlignment(big_points_info, Qt.AlignCenter)
            Layout_info.setAlignment(small_points_info, Qt.AlignCenter)

            Layout.addLayout(Layout_info)


            for j in range(tables[i]):
                #########################################################
                # layout gracza
                Layout_Players = QHBoxLayout()

                player_label = self.main_window.create_player_label(players[player_cnt].get("name"),j+1)
                player_label.setFixedWidth(100)
                player_label.setWordWrap(True)
                Layout_Players.addWidget(player_label)

                Big_points = self.main_window.create_line_edit()
                # Big_points.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                validator = QRegularExpressionValidator(QRegularExpression("([0-9]|[1-9][0-9]|[1-9][0-9][0-9])"))
                Big_points.setMaximumWidth(100)
                Big_points.setValidator(validator)
                Big_points.textChanged.connect(lambda text, player = player_cnt: self.big_points_change(player, text))
                
                Small_points = self.main_window.create_line_edit()
                # Small_points.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                Small_points.setMaximumWidth(100)
                Small_points.setValidator(validator) 
                Small_points.textChanged.connect(lambda text, player = player_cnt: self.small_points_change(player, text))
                
                Layout_Players.addWidget(Big_points)
                Layout_Players.addWidget(Small_points)

                Layout_Players.setAlignment(player_label, Qt.AlignLeft)
                Layout_Players.setAlignment(Big_points, Qt.AlignCenter)
                Layout_Players.setAlignment(Small_points, Qt.AlignCenter)
                
                player_cnt += 1

                Layout.addLayout(Layout_Players)

            Layout.addSpacing(20)

        return Layout

    # def clear_layout(self):
    #     self.main_window.clear_layout(self)

    def big_points_change(self,player_cnt,text):
        if text:
            self.main_window.big_points_change(player_cnt,int(text))


    def small_points_change(self,player_cnt,text):
        if text:
            self.main_window.small_points_change(player_cnt,int(text))
    
    def filed_check(self):
        all_filed = self.main_window.filed_check()

        #########################################################
        # jezeli nie wszystkie pola z punktami zostaly uzupelnione
        if all_filed is False:
            self.main_window.show_warning( self.main_window.get_text("Error"), self.main_window.get_text("Points_Not_Filed"))
        else:
        #########################################################
        # zakomunikuj ze wszystkie pola sa uzupelnione
            self.main_window.ready_to_calculate_result()

    #########################################################
    # Funkcja ktora dla Playoff wyswietla komunikat z ktorych miejsc przechodza osoby
    # do nastepnej rundy
    def advancing_players_information(self, advancing_places, lucky_loosers, waiting):
        # advancing_places,lucky_loosers = self.main_window.advancing_players()
        text = self.main_window.get_text("Places_From_Tables_That_Advance") 
        for i in range(1,advancing_places):
            text += str(i) + ","
        text += str(advancing_places) + ".\n"
        text += self.main_window.get_text("Lucky_Loosers") + str(advancing_places+1)+self.main_window.get_text("Place") + str(lucky_loosers) + ".\n"
        if waiting:
            text += self.main_window.get_text("Waiting_In_Next_Round")
        self.main_window.show_information(self.main_window.get_text("Advancing_Players_Information"), text)


    def last_round_information(self):
        text = self.main_window.get_text("Last_Round_Note") 
        self.main_window.show_information(self.main_window.get_text("Last_Round_Information"), text)


    def resize(self,width,height):
        """zmiana wielkosci przyciskow przy zmianie rozmiaru okna CT"""
        pass

