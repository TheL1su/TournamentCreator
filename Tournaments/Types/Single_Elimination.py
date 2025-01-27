from Tournaments.Player import Players
import math

class Single_Elimination():
    #IF min i max przy stole = 2
    def __init__(self):
        pass
    def create_tables(self, players, tables):
        players.shuffle()
        players.table_sort(seats=False)
        table = 0
        seat = 0
        for player in players.list:
            if seat >= tables[table]:
                player.add_table(-1,-1)
                player.big_points_change(0)
                player.small_points_change(0)
            else:
                player.add_table(table, seat)
                table += 1
                if table >= len(tables):
                    table = 0
                    seat += 1

        players.table_sort()
        pass

    def result(self,players):

        num_of_players = len(players.list)
        players.list.sort(key=lambda x: (x.curr_big_points,x.curr_small_points), reverse=True)
        players.list.sort(key=lambda x: x.tables[-1][0])

        advancing_players = Players()
        place_at_table = 1
        table = 0
        maybe_lucky_looser = Players()
        lucky_looser_place = self.advancing_places + 1
        for i in range(num_of_players):
            if players.list[i].tables[-1][0] == -1:
                advancing_players.add_player(players.list[i])
            else:
                # Jezeli przechodzimy do kolejnego stolika to wyzeruj pozycje 
                if(players.list[i].tables[-1][0] != table):
                    place_at_table = 1

                # Jezeli pozycja na stole gwarantuje przejscie do nastepnej rundy
                if(place_at_table <= self.advancing_places):
                    advancing_players.add_player(players.list[i])
                # Dodaj do potencjalnej listy lucky looser
                elif place_at_table == lucky_looser_place:
                    maybe_lucky_looser.add_player(players.list[i])
                
                place_at_table += 1
                table = players.list[i].tables[-1][0]
        
        maybe_lucky_looser.list.sort(key=lambda x:  (x.curr_big_points,x.curr_small_points), reverse=True)
        for i in range(self.lucky_loosers):
            advancing_players.add_player(maybe_lucky_looser.list[i])
        
        #####################################################
        # usuwa lucky_loosers z listy, zostają "unlucky_loosers"
        for i in range(self.lucky_loosers):
            maybe_lucky_looser.list.pop(0)


        return advancing_players,maybe_lucky_looser
    



    #####################################################
    # zwraca ilość stolików i ilość osób przy każdym stoliku
    def count_tables(self,num_of_players,min_at_table,max_at_table, new_tournament=False):
        next_players = num_of_players if new_tournament else math.ceil(num_of_players/2)
        tables = self.try_to_divide(next_players, min_at_table, max_at_table)
        while not tables:
            next_players += -1 if new_tournament else 1
            tables = self.try_to_divide(next_players, min_at_table, max_at_table)

        return tables

    #####################################################
    # czy daną ilość graczy można podzielić na stoliki
    def try_to_divide(self,num_of_players,min_at_table,max_at_table):
        players_at_tables = max_at_table
        num_of_tables = math.ceil(num_of_players / max_at_table)
        if num_of_players % max_at_table != 0:
            players_at_tables -=1
            num_of_tables = num_of_players // players_at_tables
            if(players_at_tables < min_at_table):
                return []
            while(num_of_players / players_at_tables < num_of_players % players_at_tables):
                players_at_tables -= 1
                num_of_tables = num_of_players // players_at_tables
                if(players_at_tables < min_at_table):
                    return []
        
        rest_of_players = num_of_players % players_at_tables 
        result = []
        cnt = 0
        for i in range(num_of_tables):
            if(cnt < rest_of_players):
                result.append(players_at_tables+1)
                cnt += 1
            else:
                result.append(players_at_tables)

        return result 
    
    #####################################################
    # ile graczy bedzie w nastepnej rundzie ze wzgledu na kolejnosc w stoliku
    def advancing_players(self,tables,next_tables, waiting):
        sum_of_next = sum(next_tables)
        advancing_from_tables = sum_of_next - waiting
        advancing_places = advancing_from_tables // len(tables)
        lucky_loosers = advancing_from_tables % len(tables)

        self.advancing_places = advancing_places
        self.lucky_loosers = lucky_loosers

        return advancing_places, lucky_loosers


