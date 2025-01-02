from Tournaments.Player import Player,Players

class Tournament:

    def __init__(self):
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

    def get_min_at_table(self):
        return self.min_at_table
    
    def get_max_at_table(self):
        return self.max_at_table

    def set_min_at_table(self,number):
        self.min_at_table = number

    def set_max_at_table(self,number):
        self.max_at_table = number

    def load_data():
        pass

    def create_tables():
        pass

    def end_round():
        pass

    def update_data():
        pass