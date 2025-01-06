from Tournaments.Player import Player,Players
from Tournaments.Types.Swiss import Swiss
from Tournaments.Types.Single_Elimination import Single_Elimination


class Tournament:

    def __init__(self,app):
        self.app = app
        self.players = Players()
        self.min_at_table = -1
        self.max_at_table = -1

    def add_player(self,player):
        name = player.split(" ")[0]
        surname = player.split(" ")[1]
        self.players.add_player(Player(name,surname))

    def add_type(self,type):
        if type == "Swiss":
            self.type = Swiss()
        elif type == "Single_Elimination":
            self.type = Single_Elimination()


    def get_min_at_table(self):
        return self.min_at_table
    
    def get_max_at_table(self):
        return self.max_at_table

    def set_min_at_table(self,number):
        self.min_at_table = number

    def set_max_at_table(self,number):
        self.max_at_table = number

    #########################################################
    # Funkcja odpowiadajaca za rozpoczecie i zarzadzanie turniejem
    def manage(self):
        #########################################################
        # Odpal layout turnieju
        self.app.tournament_layout()
        
        pass

    def load_data():
        pass

    def create_tables():
        pass

    def end_round():
        pass

    def update_data():
        pass