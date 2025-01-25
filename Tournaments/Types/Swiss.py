import random
import math

#from Type_Interface import Type_Interface


class Swiss():
    #IF 2 osoby na stolik i 9 graczy
    #IF mniej osob niz minimalna ilosc na stole

    def create_tables(self,players,tables):#,min_at_table,max_at_table,round):
        
        num_of_players = len(players.list)

        # if round != 0:
        # players.list.sort(key=lambda x: (x.big_points, x.small_points), reverse=True)
        # else:
        #     self.tables = self.count_tables(self,players,min_at_table,max_at_table)
        #     random.shuffle(players.list)

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

        

        #     players_at_tables = max_at_table


        #     if num_of_players % max_at_table == 0:
        #         num_of_tables = num_of_players / max_at_table
        #         players_at_tables = max_at_table
        #     else:
        #         while(num_of_players / players_at_tables < num_of_players % players_at_tables):
        #             players_at_tables -= 1
        #     self.num_of_tables = num_of_tables
        #     self.players_at_tables = players_at_tables
        #     self.rest_of_players = num_of_players % players_at_tables

        # cnt = 0
        # for i in range(self.num_of_tables):
        #     for j in range(self.players_at_tables):
        #         players.list[cnt] 

        # pass


    def count_tables(self,num_of_players,min_at_table,max_at_table, new=False):
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

    def end_round(self):
        pass


    