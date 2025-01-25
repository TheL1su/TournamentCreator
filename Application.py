from Language.Polski import Polski
from Language.English import English

from Window import Window

from Tournaments.Tournament import Tournament

class Application:

    def __init__(self):
        self.language = Polski()
        self.tournament = Tournament(self)
        self.window = Window(self)

    #########################################################
    # Funkcje dla Language
    def text(self, key):
        return self.language.get_text(key)
    
    def change_language(self, new_language):
        if new_language == "polski":
            self.language = Polski()
        elif new_language == "english":
            self.language = English()

    #########################################################
    # Funkcje dla Tournament Data

    def tournament_data_update(self,dictionary):
        self.tournament.data_update(dictionary)

    def save_file(self,file_):
        self.tournament.save_file(file_)
    #########################################################
    # Funkcje dla Tournament
    def tournament_add_player(self,player_name):
        self.tournament.add_player(player_name)

    def tournament_min_at_table(self):
        return self.tournament.get_min_at_table()
    
    def tournament_set_min_at_table(self,number):
        self.tournament.set_min_at_table(number)

    def tournament_max_at_table(self):
        return self.tournament.get_max_at_table()

    def tournament_set_max_at_table(self,number):
        self.tournament.set_max_at_table(number)

    def tournament_add_type(self,tournament_type):
        self.tournament.add_type(tournament_type)

    def tournament_layout(self):
        self.window.tournament_layout()

    def curr_num_of_players(self):
        return self.tournament.curr_num_of_players()
    
    def get_tables(self):
        return self.tournament.get_tables()
    
    def get_prev_tables(self):
        return self.tournament.get_prev_tables()


    def get_name(self,num):
        return self.tournament.get_name(num)
    
    def big_points_change(self,player_cnt,num):
        self.tournament.big_points_change(player_cnt,num)

    def small_points_change(self,player_cnt,num):
        self.tournament.small_points_change(player_cnt,num)

    def get_big_points(self,num):
        return self.tournament.get_big_points(num)

    def small_big_points(self,num):
        return self.tournament.small_big_points(num)

    def filed_check(self):
        return self.tournament.filed_check()
    
    def ready_to_calculate_result(self):
        self.tournament.ready_to_calculate_result()

    def get_tournament_type(self):
        return self.tournament.get_type()
    
    def load_data(self):
        self.tournament.load_data()

    def open_tournament(self, new):
        self.tournament.start_tournament(new)

    def get_players(self,players):
        return self.tournament.get_players(players)

    def result(self, type):
        self.window.result(type)

    def tables(self):
        self.window.tables()

    def advancing_players_information(self, advancing, lucky, waiting):
        self.window.advancing_players_information(advancing, lucky, waiting)

    def last_round_information(self):
        self.window.last_round_information()

    def start_new_round(self):
        self.tournament.start_round()