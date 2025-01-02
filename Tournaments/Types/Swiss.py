from Type_Interface import Type_Interface


class Swiss(Type_Interface):
    #IF 2 osoby na stolik i 9 graczy
    #IF mniej osob niz minimalna ilosc na stole

    def create_tables(self,players,min_at_table,max_at_table,round):
        
        num_of_players = len(players.list)

        if round != 0:
            players.list.sort(key=lambda x: (x.big_points, x.small_points), reverse=True)
        else:

            players_at_tables = max_at_table


            if num_of_players % max_at_table == 0:
                num_of_tables = num_of_players / max_at_table
                players_at_tables = max_at_table
            else:
                while(num_of_players / players_at_tables < num_of_players % players_at_tables):
                    players_at_tables -= 1
            self.num_of_tables = num_of_tables
            self.players_at_tables = players_at_tables
            self.rest_of_players = num_of_players % players_at_tables

        cnt = 0
        for i in range(self.num_of_tables):
            for j in range(self.players_at_tables):
                players.list[cnt] 

        pass


    def end_round(self):
        pass


    