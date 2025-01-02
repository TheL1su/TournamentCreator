from Language.Polski import Polski
from Language.English import English
from Player import Players
from Window import Window
from Tournament_Data import Tournament_Data

class Application:

    def __init__(self):
        self.language = Polski()
        self.tournament_data = Tournament_Data()
        self.players = Players()
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