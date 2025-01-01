from Language.Polski import Polski
from Language.English import English
from Player import Players
from Window import Window

class Application:

    def __init__(self):
        self.language = Polski()
        self.tournament_dict = {}
        self.players = Players()
        self.window = Window(self)

    def text(self, key):
        return self.language.get_text(key)
    
    def change_language(self, new_language):
        if new_language == "polski":
            self.language = Polski()
        elif new_language == "english":
            self.language = English()