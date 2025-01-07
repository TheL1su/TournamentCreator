from PyQt5.QtWidgets import QLineEdit,QPushButton,QGridLayout,QWidget,QFileDialog,QMessageBox,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QIntValidator


class Single_Elimination_Layout(QGridLayout):


    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        #########################################################
        # Przyciski nastepna runda, zapisz i wyjdz
        self.Submit_Round = QPushButton(self.main_window.get_text("Next_Round"))
        self.Submit_Round.connect(self.filed_check)
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
        #self.addWidget(self.Save_And_Exit,1,1)


    def add_players_and_tables(self):
        #########################################################
        # Layout stolikow 
        Layout = QVBoxLayout()
        num_of_players = self.main_window.num_of_players()
        
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
        
    """
    #########################################################
    # Funkcja do sprawedzania czy wpisano ilosc rozgrywek w rundzie
    def Game_Num(self):
        number = self.Game_Num.text()
        if not number:
            QMessageBox.warning(self.main_window, self.main_window.get_text("Error"), self.main_window.get_text("Specify_Value_For_Round"))
    """