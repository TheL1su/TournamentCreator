from PyQt5.QtWidgets import QMainWindow, QWidget
from Widgets import Widgets
from PyQt5.QtGui import QColor
from Layouts.Start_Layout import Start_Layout
from Layouts.New_Tournament_Layout import New_Tournament_Layout
from Layouts.Continue_Tournament_Layout import Continue_Tournament_Layout
from Layouts.Single_Elimination_Layout import Single_Elimination_Layout
from Layouts.Swiss_Layout import Swiss_Layout
class Window(QMainWindow):

    def __init__(self, app):
        self.app = app
        super().__init__()
        
        #########################################################
        #default Geometria
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle(self.app.text("Title"))
        self.widgetsStyle = Widgets()

        #########################################################
        # Kolor tla
        Color = self.palette()
        Color.setColor(self.backgroundRole(), QColor(41,44,51))
        self.setPalette(Color)

        #########################################################
        # Layout startowy
        self.layout = Start_Layout(self)
        self.Central_widget = QWidget(self)
        self.set_widget()
        self.show()

    #########################################################
    # Ustawianie tytulu
    def set_title(self):
        self.setWindowTitle(self.app.text("Title"))

    #########################################################
    # Ustawianie centralnego widgetu
    def set_widget(self):
        self.Central_widget.setLayout(self.layout)
        self.setCentralWidget(self.Central_widget)

    def delete_later(self):
        self.Central_widget.deleteLater()
        self.Central_widget = QWidget(self)

    def resizeEvent(self,event):
        self.layout.resize(self.width(),self.height())

    #########################################################
    # Funkcje dla jezyka
    def get_text(self, key):
        return self.app.text(key)
    
    def change_language(self, language):
        self.app.change_language(language)

    #########################################################
    # Funkcje dla Stylu
    def create_label(self,text):
        label = self.get_text(text)
        return self.widgetsStyle.create_label(label)
    
    def create_table_label(self, num):
        if num == 1:
            label = self.get_text("Table_And_Points")
        else:
            label = self.get_text("Table") + str(num)
        return self.widgetsStyle.create_label(label)
    
    def create_player_label(self, name, num):
        label = str(num) + ". " + name
        return self.widgetsStyle.create_label(label)

    def create_tool_button(self,text,menu):
        label = self.get_text(text)
        return self.widgetsStyle.create_tool_button(parent = self,text = label,menu = menu)

    #########################################################
    # Funkcje dla tournament data
    def key_check(self,key):
        return self.app.key_check(key)
    
    def get_value(self,key):
        return self.app.get_value(key)

    def tournament_data_update(self,dictionary):
        self.app.tournament_data_update(dictionary)

    #########################################################
    # Funkcje dla tournament
    def tournament_add_player(self,player_name):
        self.app.tournament_add_player(player_name)

    def tournament_min_at_table(self):
        return self.app.tournament_min_at_table()

    def tournament_set_min_at_table(self,number):
        self.app.tournament_set_min_at_table(number)

    def tournament_max_at_table(self):
        return self.app.tournament_max_at_table()
    
    def tournament_set_max_at_table(self,number):
        self.app.tournament_set_max_at_table(number)

    def tournament_add_type(self,tournament_type):
        self.app.tournament_add_type(tournament_type)

    def get_tables(self):
        return self.app.get_tables()

    def num_of_players(self):
        return self.app.num_of_players()
    
    def get_name(self,num):
        return self.app.get_name(num)

    def big_points_change(self,player_cnt,num):
        self.app.big_points_change(self,player_cnt,num)

    def small_points_change(self,player_cnt,num):
        self.app.small_points_change(self,player_cnt,num)

    def filed_check(self):
        return self.app.filed_check()

    #########################################################
    # Tworzenie nowych layoutow
    def new_tournament(self):
        self.delete_later()
        self.layout = New_Tournament_Layout(self)
        self.set_widget()
        self.show()

    def continue_tournament(self):
        self.delete_later()
        self.layout = Continue_Tournament_Layout(self)
        self.set_widget()
        self.show()

    #########################################################
    # do poprawy
    def tournament_layout(self):
        self.delete_later()
        self.layout = Single_Elimination_Layout(self)
        self.set_widget()
        self.show()


    #########################################################
    # wyczysc layout
    def clear_layout(self,layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                sub_layout = item.layout()
                if sub_layout:
                    self.clear_layout(sub_layout)
