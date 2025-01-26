#from Type_Interface import Type_Interface
from Tournaments.Player import Player,Players
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
        print(len(tables))
        for player in players.list:
            print("Seat and table: ", seat, table)
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

        # for i in range(len(advancing_players.list)):
        #     advancing_players.list[i].pt()

        # for i in range(len(maybe_lucky_looser.list)):
        #     maybe_lucky_looser.list[i].pt()


        return advancing_players,maybe_lucky_looser
    



        #####################################################
        # TODO 
    def count_tables_(self,num_of_players,min_at_table,max_at_table):
        # num_of_players = len(players.list)

        # if num_of_players % max_at_table == 0:
        num_of_tables = math.ceil(num_of_players / max_at_table)
        players_at_tables = max_at_table
        if num_of_players % max_at_table != 0:
            # players_at_tables = max_at_table
            players_at_tables -= 1
            num_of_tables = num_of_players // players_at_tables
            while(num_of_tables < num_of_players % players_at_tables):
                players_at_tables -= 1
                num_of_tables = num_of_players // players_at_tables
        self.num_of_tables = num_of_tables
        self.players_at_tables = players_at_tables
        self.rest_of_players = num_of_players % players_at_tables

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
        # if num_of_players % max_at_table == 0:
        num_of_tables = math.ceil(num_of_players / max_at_table)
            # players_at_tables = max_at_table
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



# test = Single_Elimination()

# Gracz1 = Player("A","A")
# Gracz1.big_points = 2
# Gracz1.small_points = 13
# Gracz1.tables = [1]

# Gracz2 = Player("B","B")
# Gracz2.big_points = 3
# Gracz2.small_points = 7
# Gracz2.tables = [1]

# Gracz3 = Player("C","C")
# Gracz3.big_points = 1
# Gracz3.small_points = 6
# Gracz3.tables = [1]

# Gracz4 = Player("D","D")
# Gracz4.big_points = 4
# Gracz4.small_points = 2
# Gracz4.tables = [2]

# Gracz5 = Player("E","E")
# Gracz5.big_points = 3
# Gracz5.small_points = 1
# Gracz5.tables = [2]

# Gracz6 = Player("F","F")
# Gracz6.big_points = 2
# Gracz6.small_points = 6
# Gracz6.tables = [2]

# Gracz7 = Player("G","G")
# Gracz7.big_points = 1
# Gracz7.small_points = 2
# Gracz7.tables = [3]

# Gracz8 = Player("H","H")
# Gracz8.big_points = 3
# Gracz8.small_points = 2
# Gracz8.tables = [3]

# Gracz9 = Player("I","I")
# Gracz9.big_points = 5
# Gracz9.small_points = 6
# Gracz9.tables = [3]



# lista = Players()

# lista.add_player(Gracz1)
# lista.add_player(Gracz2)
# lista.add_player(Gracz3)

# lista.add_player(Gracz4)
# lista.add_player(Gracz5)
# lista.add_player(Gracz6)

# lista.add_player(Gracz7)
# lista.add_player(Gracz8)
# lista.add_player(Gracz9)

# wynik = test.result(lista,1,2)

# for i in wynik.list:
#     print(i.first_name,i.last_name)