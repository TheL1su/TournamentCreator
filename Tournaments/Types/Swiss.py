import math



class Swiss():
    #IF 2 osoby na stolik i 9 graczy
    #IF mniej osob niz minimalna ilosc na stole

    def create_tables(self,players,tables):
        result = []
        start = 0
        for table_num, table in enumerate(tables):
            cur_table = players.list[start:start+table]
            cur_table.sort(reverse = True, key = lambda x: sum([table[1] for table in x.tables]))
            for seat_num, player in enumerate(cur_table):
                player.add_table(table_num,seat_num)
            players.list[start:start+table] = cur_table
            result += cur_table
            start += table



    def count_tables(self,num_of_players,min_at_table,max_at_table, new_tournament=False):
        num_of_tables = math.ceil(num_of_players / max_at_table)
        players_at_tables = max_at_table
        if num_of_players % max_at_table != 0:
            players_at_tables -= 1
            num_of_tables = num_of_players // players_at_tables
            if players_at_tables < min_at_table:
                return []

            while(num_of_tables < num_of_players % players_at_tables):
                players_at_tables -= 1
                num_of_tables = num_of_players // players_at_tables
                if players_at_tables < min_at_table:
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
   