from PyQt5.QtWidgets import QLineEdit,QPushButton,QGridLayout,QWidget,QFileDialog,QMessageBox,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QIntValidator


class Single_Elimination_Layout(QGridLayout):


    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        #########################################################
        # Przyciski nastepna runda, zapisz i wyjdz
        self.Submit_Round = QPushButton(self.main_window.get_text("Submit_Round"))
        self.Submit_Round.connect(self.filed_check)
        self.Next_Round.QPushButton(self.main_window.get_text("Next_Round"))
        self.Save_And_Exit = QPushButton(self.main_window.get_text("Save_And_Exit"))


        """
        #########################################################
        # Przyciski do wprowadzania ilosci rozgrywek w pojedynczej rundzie
        self.Game_Num = QLineEdit()
        self.Game_Num.setValidator(QIntValidator(1,20))
        self.Submit_Game_Num = QPushButton(self.main_window.get_text("Submit"))
        """
        
    def add_buttons(self):
        #########################################################
        # Layout
        Layout_Tables = self.add_players_and_tables()

        self.addLayout(Layout_Tables)
        self.addWidget(self.Submit_Round,1,0)

        self.show()
        #self.addWidget(self.Save_And_Exit,1,1)


    def add_players_and_tables(self):
        #########################################################
        # Layout stolikow 
        Layout = QVBoxLayout()
        num_of_players = self.main_window.curr_num_of_players()
        
        #########################################################
        # ilos stolikow
        tables = self.main_window.get_tables()
        
        #########################################################
        # ilos graczy
        player_cnt = 0
        
        for i in range(len(tables)):
            
            #########################################################
            # Label stolika
            table_number = self.main_window.create_table_label(i+1)
            Layout.addWidget(table_number)


            for j in range(tables[i]):
                #########################################################
                # layout gracza
                Layout_Players = QHBoxLayout()

                name = self.main_window.get_name(player_cnt)
                player_label = self.main_window.create_player_label(name,j)
                Layout_Players.addWidget(player_label)

                Big_points = QLineEdit()
                Big_points.setValidator(QIntValidator(1,1000))
                Big_points.textChanged.connect(lambda text: self.big_points_change(player_cnt, text))
                
                Small_points = QLineEdit()
                Small_points.setValidator(QIntValidator(1,1000)) 
                Small_points.textChanged.connect(lambda text: self.small_points_change(player_cnt, text))
                
                Layout_Players.addWidget(Big_points)
                Layout_Players.addWidget(Small_points)
                
                player_cnt += 1

                Layout.addWidget(Layout_Players)

        return Layout

    # def clear_layout(self):
    #     self.main_window.clear_layout(self)

    def big_points_change(self,player_cnt,text):
        self.main_window.big_points_change(player_cnt,int(text))


    def small_points_change(self,player_cnt,text):
        self.main_window.small_points_change(player_cnt,int(text))
    
    def filed_check(self):
        all_filed = self.main_window.filed_check()

        #########################################################
        # jezeli nie wszystkie pola z punktami zostaly uzupelnione
        if all_filed is False:
            QMessageBox.warning(self.main_window, self.main_window.get_text("Error"), self.main_window.get_text("Points_Not_Filed"))
        else:
        #########################################################
        # zakomunikuj ze wszystkie pola sa uzupelnione
            self.main_window.ready_to_calculate_result()

    #########################################################
    # Funkcja ktora dla Playoff wyswietla komunikat z ktorych miejsc przechodza osoby
    # do nastepnej rundy
    def advancing_players_information(self):
        advancing_places,lucky_loosers = self.main_window.advancing_players()
        text = self.main_window.get_text("Places_From_Tables_That_Advance") 
        for i in range(1,advancing_places):
            text += str(i) + ","
        text += str(advancing_places) + "\n"
        text += self.main_window.get_text("Lucky_Loosers") + str(advancing_places)+self.main_window.get_text("Place") + str(lucky_loosers) + "."
        QMessageBox.information(self, self.main_window.get_text("Advancing_Players_Information"), text)

    #########################################################
    # layout wynikow dla playoff
    def single_elimination_result(self):
        #########################################################
        # wyczysc layout
        self.main_window.clear_layout(self)
        Layout = QVBoxLayout()
        num_of_players = self.main_window.get_prev_tables()

        self.addLayout(Layout)
        self.addWidget(self.Next_Round,1,0)
        self.addWidget(self.Save_And_Exit,1,1)
        self.show()

    #########################################################
    # layout wynikow dla swiss    
    def swiss_result(self):
        #########################################################
        # wyczysc layout
        self.main_window.clear_layout(self)
        Layout = QVBoxLayout()
        num_of_players = self.main_window.curr_num_of_players()
        
        ranking = self.main_window.create_label("Ranking")
        Layout.addWidget(ranking)

        Legend = QHBoxLayout()
        Players = self.main_window.create_label("Player")
        Big_points = self.main_window.create_label("Big_points")
        Small_points = self.main_window.create_label("Small_points")
        Legend.addWidget(Players)
        Legend.addWidget(Big_points)
        Legend.addWidget(Small_points)
        Layout.addWidget(Legend)

        for i in range(num_of_players):
            Layout_Players = QHBoxLayout()

            name = self.main_window.get_name(i)
            player_label = self.main_window.create_player_label(name,i+1)
            
            big_points = self.main_window.get_big_points(i)
            big = self.main_window.create_label(big_points)

            small_points = self.main_window.get_small_points(i)
            small = self.main_window.create_label(small_points)

            Layout_Players.addWidget(player_label)
            Layout_Players.addWidget(big)
            Layout_Players.addWidget(small)

            Layout.addWidget(Layout_Players)
            
        self.addLayout(Layout)
        self.addWidget(self.Next_Round,1,0)
        self.addWidget(self.Save_And_Exit,1,1)
        self.show()

    """
    #########################################################
    # Funkcja do sprawedzania czy wpisano ilosc rozgrywek w rundzie
    def Game_Num(self):
        number = self.Game_Num.text()
        if not number:
            QMessageBox.warning(self.main_window, self.main_window.get_text("Error"), self.main_window.get_text("Specify_Value_For_Round"))
    """