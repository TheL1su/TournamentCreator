import json

class Tournament_Data:
    def __init__(self,tournament):
        self.tournament = tournament
        self.data = {}

    #########################################################
    # Funkcja sprawdzajaca czy klucz istnieje w slowniku 
    def key_check(self,key):
        if key in self.data:
            return True
        else:
            return False
        

    #########################################################
    # Funkcja zwracajaca wartosc dla klucza
    def get_value(self,key):
        return self.data.get(key)
    
    #########################################################
    # Funkcja wykonujaca update na slowniku
    def update(self,dictionary):
        self.data.update(dictionary)

    def load_players(self,players):
        for i in self.data.get("Players"):
            players.load_player(i["first_name"],
                                i["last_name"],
                                i["big_points"],
                                i["small_points"],
                                i["curr_big_points"],
                                i["curr_small_points"],
                                i["tables"],
                                i["id"]
                                )

    def load_current_players(self,players,current_players):
        for i in self.data.get("Current_Players"):
            player = players.get_player_by_id(i["id"])
            current_players.add_player(player)

    def save_file(self,file_):
        json.dump(self.data, file_, indent=4, ensure_ascii=False)