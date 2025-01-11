
class Player:
    def __init__(self, first, last,big_points=0,small_points=0,curr_big_points=-1,curr_small_points=-1,tables=[],id_=-1):
        self.first_name = first
        self.last_name = last
        self.big_points = big_points
        self.small_points = small_points
        self.curr_big_points = curr_big_points
        self.curr_small_points = curr_small_points
        self.tables = tables
        self.id = id_

    def filed_check(self):
        if self.curr_big_points == -1 or self.curr_small_points == -1:
            return False
        return True

    def set_id(self,id_):
        self.id = id_

    def get_id(self):
        return self.id

    def update_points(self):
        self.big_points += self.curr_big_points
        self.small_points += self.curr_small_points
        self.curr_big_points = -1
        self.curr_small_points = -1

    #########################################################
    # Funkcja testowa do wypisywania graczy
    def pt(self):
        print(self.first_name,
        self.last_name,
        self.big_points,
        self.small_points,
        self.curr_big_points,
        self.curr_small_points,
        self.tables,
        self.id)
        print()
        
class Players:
    def __init__(self):
        self.list = list()

    def add_player(self, player):
        if(player.get_id()==-1):
            player.set_id(len(self.list))
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
    
    def save_players(self):
        players_data = []
        for i in self.list:
            player_data = {"first_name" : i.first_name,
                           "last_name" : i.last_name,
                           "big_points" : i.big_points,
                           "small_points" : i.big_points,
                           "curr_big_points" : i.curr_big_points,
                           "curr_small_points" : i.curr_small_points,
                           "tables" : i.tables,
                           "id" : i.id}
            players_data.append(player_data)
        return players_data
    
    def load_player(self,first_name,last_name,big_points,small_points,curr_big_points,curr_small_points,tables,id_):
        self.add_player(Player(first_name,last_name,big_points,small_points,curr_big_points,curr_small_points,tables,id_))
    
    def get_player_by_id(self,id_):
        for i in self.list:
            if(i.get_id() == id_):
                return i

    def update_points(self):
        for i in self.list:
            i.update_points()