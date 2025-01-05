from Type_Interface import Type_Interface
import math

class Single_Elimination(Type_Interface):
    #IF min i max przy stole = 2

    def create_tables(self,players,min_at_table,max_at_table,round):
        num_of_players = len(players.list)
        if round == 0:
            number_of_rounds = math.ceil(math.log(num_of_players,2))
            num_of_byes = 2**number_of_rounds - num_of_players
