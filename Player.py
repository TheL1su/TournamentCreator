class Player:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.big_point = 0
        self.small_points = 0



    
class Players:
    def __init__(self):
        self.list = list()

    def add_player(self, player):
        self.list.append(player)