from Type_Interface import Type_Interface
import math

class Single_Elimination(Type_Interface):
    #IF min i max przy stole = 2

    def create_tables(self,players,min_at_table,max_at_table,round):
        num_of_players = len(players.list)

    #####################################################
    # czy daną ilość graczy mżna podzielić na stoliki
    def try_to_divide(self,num_of_players,min_at_table,max_at_table):
        players_at_tables = max_at_table
        if num_of_players % max_at_table == 0:
            num_of_tables = num_of_players / max_at_table
            players_at_tables = max_at_table
        else:
            while(num_of_players / players_at_tables < num_of_players % players_at_tables):
                players_at_tables -= 1
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
    def advancing_players(self,tables,next_tables):
        sum_of_next = sum(next_tables)
        advancing_places = sum_of_next // len(tables)
        lucky_loosers = sum_of_next % len(tables)

        return advancing_places, lucky_loosers
