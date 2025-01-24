import random

class Player:
    def __init__(self, first, last,big_points=0,small_points=0,curr_big_points=-1,curr_small_points=-1,tables=[],id_=-1):
        self.first_name = first
        self.last_name = last
        self.big_points = big_points
        self.small_points = small_points
        self.curr_big_points = curr_big_points
        self.curr_small_points = curr_small_points
        if tables:
            self.tables = tables
        else:
            self.tables = list()
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

    def add_table(self, table, seat):
        self.tables.append((table,seat))
        
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

    def swiss_sort(self):
        self.list.sort(key=lambda x: (x.big_points, x.small_points), reverse=True)

    def single_elimination_sort(self):
        self.list.sort(key=lambda x: (x.curr_big_points,x.curr_small_points), reverse=True)
        self.list.sort(key=lambda x: x.tables[-1])

    def get_players(self):
        return [ {"name": player.first_name +" " + player.last_name, 
                  "big_points": player.big_points, 
                  "small_points": player.small_points,
                  "curr_big": player.curr_big_points,
                  "curr_small": player.curr_small_points} 
                  for player in self.list ]
    
    def copy(self, other):
        self.list = [player for player in other.list]

    def shuffle(self):
        random.shuffle(self.list)

    def table_sort(self, seats=True):
        if seats:
            self.list.sort(key=lambda x: x.tables[-1])

        else:
            self.list.sort(key=lambda x: x.tables[-1][0])
