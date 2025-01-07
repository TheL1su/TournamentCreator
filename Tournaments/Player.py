
class Player:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.big_points = 0
        self.small_points = 0
        self.curr_big_points = -1
        self.curr_small_points = -1
        self.tables = []

    def filed_check(self):
        if self.curr_big_points == -1 or self.curr_small_points == -1:
            return False
        return True

class Players:
    def __init__(self):
        self.list = list()

    def add_player(self, player):
        self.list.append(player)

    def num_of_players(self):
        return len(self.list)
    
    def get_name(self,num):
        return self.list[num].first_name+self.list[num].last_name 
    
    def big_points_change(self,player_cnt,num):
        self.list[player_cnt].curr_big_points = num

    def small_points_change(self,player_cnt,num):
        self.list[player_cnt].curr_small_points = num

    def filed_check(self):
        return all([player.filed_check() for player in self.list])