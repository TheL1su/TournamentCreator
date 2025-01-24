from PyQt5.QtWidgets import QMainWindow, QWidget
from Widgets import Widgets
from MessageBoxes import MessageBoxFactory
from PyQt5.QtGui import QColor
from Layouts.Start_Layout import Start_Layout
from Layouts.New_Tournament_Layout import New_Tournament_Layout
from Layouts.Continue_Tournament_Layout import Continue_Tournament_Layout
from Layouts.Tournament_Layout import Tournament_Layout
from Layouts.Swiss_Layout import Swiss_Layout
from Layouts.Swiss_Result_Layout import Swiss_Result_layout
import os

class Window(QMainWindow):

    def __init__(self, app):
        self.app = app
        super().__init__()
        
        #########################################################
        #default Geometria
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle(self.app.text("Title"))


        #########################################################
        # Tlo aplikacji
        # current_directory = os.path.dirname(os.path.abspath(__file__))
        # # Specify the filename you're checking
        # filename = 'test123.png'
        # # Create the full path to the file
        # file_path = os.path.join(current_directory, filename)
        # if os.path.exists(file_path): 
        #     print("halo znalazlo mnie")
        # else: print(f"File '{filename}' does not exist in the same directory as the Python program.")
        # self.setStyleSheet(f"QMainWindow {{background-image: url({file_path}); background-repeat: no-repeat; background-position: center;}}")
        # self.setStyleSheet("QMainWindow {background-image: url('background.png'); background-repeat: no-repeat; background-position: center;}")

        #########################################################
        # Fabryki widgetow i messageboxow
        self.widgetsStyle = Widgets()
        self.messageboxFactory = MessageBoxFactory()

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
    
    def create_num_label(self,num):
        return self.widgetsStyle.create_label(str(num))

    def create_tool_button(self,text,menu):
        label = self.get_text(text)
        return self.widgetsStyle.create_tool_button(parent = self,text = label,menu = menu)

    #########################################################
    # Funkcje dla MessageBoxa
    def show_information(self,title, message):
        self.messageboxFactory.show_information(self,title,message)

    def show_warning(self,title,message):
        self.messageboxFactory.show_warning(self,title,message)

    def show_question(self,title,message):
        self.messageboxFactory.show_question(self,title,message)
    #########################################################
    # Funkcje dla tournament data

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

    def get_prev_tables(self):
        return self.app.prev_tables()

    def curr_num_of_players(self):
        return self.app.curr_num_of_players()
    
    def get_name(self,num):
        return self.app.get_name(num)

    def big_points_change(self,player_cnt,num):
        self.app.big_points_change(player_cnt,num)

    def small_points_change(self,player_cnt,num):
        self.app.small_points_change(player_cnt,num)

    def get_big_points(self,num):
        return self.app.get_big_points(num)

    def small_big_points(self,num):
        return self.app.small_big_points(num)

    def filed_check(self):
        return self.app.filed_check()
    
    def ready_to_calculate_result(self):
        self.app.ready_to_calculate_result()
    
    def get_tournament_type(self):
        return self.app.get_tournament_type()

    def load_data(self):
        self.app.load_data()

    def open_tournament(self, *, new):
        self.delete_later()
        self.layout = Tournament_Layout(self)
        self.set_widget()
        self.app.open_tournament(new)

    #########################################################
    # Zapisz plik json
    def save_file(self,file_):
        self.app.save_file(file_)


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
        self.layout = Tournament_Layout(self)
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

    def get_players(self):
        return self.app.get_players()

    def result(self, type):
        self.delete_later()
        if type == "Swiss":
            self.layout = Swiss_Result_layout(self)
        self.set_widget()
        self.show()


    def tables(self):
        self.layout.add_widgets()

    def advancing_players_information(self, advancing, lucky):
        self.layout.advancing_players_information(advancing, lucky)

    def start_new_round(self):
        self.delete_later()
        self.layout = Tournament_Layout(self)
        self.app.start_new_round()
        self.set_widget()
        self.show()
