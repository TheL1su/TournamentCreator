from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout

class Single_Elimination_Result_layout(QVBoxLayout):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        #########################################################
        # Przyciski nastepna runda, zapisz i wyjdz
        self.Next_Round = self.main_window.create_push_button("Next_Round")
        self.Next_Round.clicked.connect(self.start_next_round)
        self.Save_And_Exit = self.main_window.create_push_button("Save_And_Exit")
        self.Save_And_Exit.clicked.connect(self.main_window.save_exit)
        self.Exit = self.main_window.create_push_button("End_And_Exit")
        self.Exit.clicked.connect(self.main_window.confirm_exit)

        #########################################################
        # Layout
        Layout_Tables, last_round = self.add_players_and_tables()

        self.addStretch()
        self.addLayout(Layout_Tables)
        self.addStretch()


        if last_round:
            self.addWidget(self.Exit)
        
        else:
            buttons_layout = QHBoxLayout()
            buttons_layout.addWidget(self.Next_Round)
            buttons_layout.addWidget(self.Save_And_Exit)
            self.addLayout(buttons_layout)


    def add_players_and_tables(self):
        #########################################################
        # Layout stolikow 
        Layout = QVBoxLayout()
        players = self.main_window.get_players()
        advancing_players = self.main_window.get_players("advancing_players")
        advancing_id = [player.get("id") for player in advancing_players]

        
        #########################################################
        # ilos stolikow
        tables = self.main_window.get_tables()
        last_round = len(tables) == 1 and players[0].get("table")[0] != -1
        
        #########################################################
        # ilos graczy
        player_cnt = 0
        if players[player_cnt].get("table")[0] == -1:
            waitnig_label = self.main_window.create_label("Waiting_Players",bold=True)
            Layout.addWidget(waitnig_label)


        while players[player_cnt].get("table")[0] == -1:
            player_label = self.main_window.create_player_label(players[player_cnt].get("name"),player_cnt+1,bold=True,color="green")
            player_label.setFixedWidth(100)
            player_label.setWordWrap(True)
            Layout.addWidget(player_label)
            player_cnt += 1

        Layout.addSpacing(50)

        
        for i in range(len(tables)):
            #########################################################
            # Label stolika
            table_number = self.main_window.create_table_label(i+1)
            Layout.addWidget(table_number)

            Layout_Info = QHBoxLayout()
            player = self.main_window.create_label("Player", bold=True)
            player.setFixedWidth(200)
            big = self.main_window.create_label("Big_Points",bold=True)
            big.setFixedWidth(200)
            small = self.main_window.create_label("Small_Points",bold=True)
            small.setFixedWidth(200)
            Layout_Info.addWidget(player)
            Layout_Info.addWidget(big)
            Layout_Info.addWidget(small)
            Layout.addLayout(Layout_Info)


            is_advancing = True
            if last_round:
                color = "white"
                is_advancing = False
            else:
                is_advancing = True
                color = "green"
                advancing_label = self.main_window.create_label("Advancing", bold = True)
                eliminated_label = self.main_window.create_label("Eliminated", bold = True)
                Layout.addWidget(advancing_label)
            
            for j in range(tables[i]):
                #########################################################
                # layout gracza

                if is_advancing and players[player_cnt].get("id") not in advancing_id:
                    is_advancing = False
                    color = "red"
                    Layout.addWidget(eliminated_label)

                Layout_Players = QHBoxLayout()

                player_label = self.main_window.create_player_label(players[player_cnt].get("name"),j+1,bold=is_advancing, color=color)
                player_label.setFixedWidth(200)
                player_label.setWordWrap(True)
                Layout_Players.addWidget(player_label)

                Big_points = self.main_window.create_num_label(players[player_cnt].get("curr_big"), bold=is_advancing, color=color)
                Big_points.setMaximumWidth(200)
                Small_points = self.main_window.create_num_label(players[player_cnt].get("curr_small"), bold=is_advancing, color=color)
                Small_points.setMaximumWidth(200)
                
                Layout_Players.addWidget(Big_points)
                Layout_Players.addWidget(Small_points)
                
                player_cnt += 1

                Layout.addLayout(Layout_Players)

        return Layout, last_round


    def start_next_round(self):
        self.main_window.start_new_round()

    def resize(self,width,height):
        """zmiana wielkosci przyciskow przy zmianie rozmiaru okna CT"""
        pass
