from Language.Polski import Polski
from Language.English import English

from Window import Window
from Tournament_Data import Tournament_Data
from Tournaments.Tournament import Tournament

class Application:

    def __init__(self):
        self.language = Polski()
        self.tournament_data = Tournament_Data()
        self.tournament = Tournament()
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
    def key_check(self,key):
        return self.tournament_data.key_check(key)

    def get_value(self,key):
        return self.tournament_data.get_value(key)

    def tournament_data_update(self,dictionary):
        self.tournament_data.update(dictionary)

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