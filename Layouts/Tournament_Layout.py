from PyQt5.QtWidgets import QLineEdit,QPushButton,QGridLayout,QWidget,QFileDialog,QMessageBox,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QIntValidator
import copy


class Tournament_Layout(QGridLayout):


    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        #########################################################
        # Przyciski nastepna runda, zapisz i wyjdz
        self.Submit_Round = QPushButton(self.main_window.get_text("Submit_Round"))
        self.Submit_Round.clicked.connect(self.filed_check)
        self.Next_Round = QPushButton(self.main_window.get_text("Next_Round"))
        self.Next_Round.clicked.connect(self.start_next_round)
        self.Save_And_Exit = QPushButton(self.main_window.get_text("Save_And_Exit"))
        self.Save_And_Exit.clicked.connect(self.save_exit)

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

        self.addLayout(Layout_Tables,0,0)
        self.addWidget(self.Submit_Round,1,0)

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
        
        for i in range(len(tables)):
            
            #########################################################
            # Label stolika
            table_number = self.main_window.create_table_label(i+1)
            Layout.addWidget(table_number)


            for j in range(tables[i]):
                #########################################################
                # layout gracza
                Layout_Players = QHBoxLayout()

                player_label = self.main_window.create_player_label(players[player_cnt].get("name"),j+1)
                Layout_Players.addWidget(player_label)

                Big_points = QLineEdit()
                Big_points.setValidator(QIntValidator(1,1000))
                Big_points.textChanged.connect(lambda text, player = player_cnt: self.big_points_change(player, text))
                
                Small_points = QLineEdit()
                Small_points.setValidator(QIntValidator(1,1000)) 
                Small_points.textChanged.connect(lambda text, player = player_cnt: self.small_points_change(player, text))
                
                Layout_Players.addWidget(Big_points)
                Layout_Players.addWidget(Small_points)
                
                player_cnt += 1

                Layout.addLayout(Layout_Players)

        return Layout

    # def clear_layout(self):
    #     self.main_window.clear_layout(self)

    def big_points_change(self,player_cnt,text):
        print(player_cnt)
        print(text)
        self.main_window.big_points_change(player_cnt,int(text))


    def small_points_change(self,player_cnt,text):
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
    def advancing_players_information(self, advancing_places, lucky_loosers):
        # advancing_places,lucky_loosers = self.main_window.advancing_players()
        text = self.main_window.get_text("Places_From_Tables_That_Advance") 
        for i in range(1,advancing_places):
            text += str(i) + ","
        text += str(advancing_places) + "\n"
        text += self.main_window.get_text("Lucky_Loosers") + str(advancing_places+1)+self.main_window.get_text("Place") + str(lucky_loosers) + "."
        self.main_window.show_information(self.main_window.get_text("Advancing_Players_Information"), text)


    #########################################################
    # WSZYSTKO POD TYM PRAWDOPODOBNIE DO USUNIĘCIA
    # przeniesione do Swiss_Result_Layout


    #########################################################
    # layout wynikow
    def result(self, type):
        # self.main_window.clear_layout(self)
        Layout = QVBoxLayout()
        #########################################################
        # layout wynikow dla playoff
        if type == "Single_Elimination":
            #########################################################
            # wyczysc layout
            num_of_players = self.main_window.get_prev_tables()

            self.addLayout(Layout)
            self.addWidget(self.Next_Round,1,0)
            self.addWidget(self.Save_And_Exit,1,1)
            self.show()

        #########################################################
        # layout wynikow dla swiss
        if type == "Swiss":
            #########################################################
            # wyczysc layout
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


    def save_exit(self):
        #########################################################
        # Otwórz okno dialogowe do zapisywania pliku
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self.main_window,
            self.main_window.get_text("Save_File"),
            "",
            self.main_window.get_text("Json_File")
            ,
            options=options
        )
        #########################################################
        # Sprawdź, czy użytkownik wybrał ścieżkę
        if file_path:
            if not file_path.endswith(".json"):
                file_path += ".json"

            #########################################################
            # Zapisz dane do pliku
            with open(file_path, 'w', encoding='utf-8') as file:
                self.main_window.save_file(file)
            self.confirm_exit()
        else: 
            self.main_window.show_warning(self.main_window.get_text("Error"),self.main_window.get_text("Path_Not_Selected"))

    def confirm_exit(self):
        #########################################################
        # Obsługa odpowiedzi użytkownika
        response = self.main_window.show_question(self.main_window.get_text("Exit"),self.main_window.get_text("Want_To_Exit"))

        if response == QMessageBox.Yes:
            self.main_window.close()  # Zamknięcie aplikacji

    def start_next_round(self):
        self.main_window.start_new_round()

    """
    #########################################################
    # Funkcja do sprawedzania czy wpisano ilosc rozgrywek w rundzie
    def Game_Num(self):
        number = self.Game_Num.text()
        if not number:
            QMessageBox.warning(self.main_window, self.main_window.get_text("Error"), self.main_window.get_text("Specify_Value_For_Round"))
    """