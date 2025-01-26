from Tournaments.Player import Player,Players
from Tournaments.Types.Swiss import Swiss
from Tournaments.Types.Single_Elimination import Single_Elimination
from Tournament_Data import Tournament_Data

class Tournament:

    def __init__(self,app):
        self.app = app
        self.players = Players()
        self.current_players = Players()
        self.advancing_players = Players()
        self.tournament_data = Tournament_Data(self)
        self.min_at_table = -1
        self.max_at_table = -1
        self.tables = []
        self.prev_tables = []
        self.next_tables = []
        self.round = 0

    def add_player(self,player):
        name = player.split(" ")[0]
        surname = player.split(" ")[1]
        self.players.add_player(Player(name,surname))

    def add_type(self,tournament_type):
        self.tournament_data.update({"Type": tournament_type})

        if tournament_type == "Swiss":
            self.type = Swiss()
            self.tournament_type_name = "Swiss"
        elif tournament_type == "Single_Elimination":
            self.type = Single_Elimination()
            self.tournament_type_name = "Single_Elimination"

    def set_type(self,type_):
        if(type_ == "Swiss"):
            self.type = Swiss()
        elif type_ == "Single_Elimination":
            self.type = Single_Elimination()

    def get_min_at_table(self):
        return self.min_at_table
    
    def get_max_at_table(self):
        return self.max_at_table

    def set_min_at_table(self,number):
        self.tournament_data.update({"Min_At_Table" : number})
        self.min_at_table = number

    def set_max_at_table(self,number):
        self.tournament_data.update({"Max_At_Table" : number})
        self.max_at_table = number

    #########################################################
    # Funkcja zwracajaca rozklad stolikow
    def get_tables(self):
        return self.tables
    
    def get_prev_tables(self):
        return self.prev_tables

    #########################################################
    # Funkcja zwracajaca liczbe graczy
    def curr_num_of_players(self):
        return self.current_players.num_of_players()
    

    #########################################################
    # Funkcja zwracajaca imie i nazwisko zawodnika
    def get_name(self,num):
        return self.current_players.get_name(num)
    
    #########################################################
    # Funkcja zmieniajaca duze punkty zawodnikowi
    def big_points_change(self,player_cnt,num):
        self.current_players.big_points_change(player_cnt,num)

    #########################################################
    # Funkcja zmieniajaca male punkty zawodnikowi
    def small_points_change(self,player_cnt,num):
        self.current_players.small_points_change(player_cnt,num)

    #########################################################
    # Funkcje zwracajace  duze i male punkty wszystkich zawodnikowi NIE ZAIMPLEMENTOWANE
    def get_big_points(self,num):
        pass

    def small_big_points(self,num):
        pass

    #########################################################
    # Funkcja sprawdzajaca czy wpisano wszystkie duze i male punkty
    def filed_check(self):
        return self.current_players.filed_check()

    #########################################################
    # Funkcja informujaca ze mozna przeliczyc wyniki rundy
    def ready_to_calculate_result(self):
        if type(self.type) == Swiss:
            self.end_swiss_round()
        
        if type(self.type) == Single_Elimination:
            self.end_single_elimination_round()
    
    def get_type(self):
        return self.tournament_type_name
    
    #########################################################
    # Funkcje dla tournament data
    def data_update(self,dictionary):
        self.tournament_data.update(dictionary)

    def save_players(self):
        players_data = self.players.save_players()
        self.tournament_data.update({"Players" : players_data})

    def save_curr_players(self):
        players_data = self.current_players.save_players()
        self.tournament_data.update({"Current_Players" : players_data})

    def save_file(self,file_):
        self.tournament_data.save_file(file_)
    #########################################################
    # Funkcja odpowiadajaca za rozpoczecie i zarzadzanie turniejem
    def manage(self):
        if self.round == 0:
            pass

        else:
            pass
        #########################################################
        # Odpal layout turnieju
        #self.app.tournament_layout()

        #########################################################
        # petla ktora czeka na wpisanie wszystkich punktow do okna
        #while self.ready_to_calculate is False:
            #timer = QTimer()
            #timer.start(1000)

        #DALEJ POLICZ WYNIK RUNDY!

        #adv,eli,new = self.type.result()
        #self.current_players = adv + new

        #if self.tournament_type_name == ""
        #    self.result_window()
        #mamy graczy -> 1 runde
        #aktualni gracze = result 1 rundy

        #aktualni gracze -> 2runda


    def load_data(self):
        #########################################################
        # zaladowanie min max i typu turnieju
        self.min_at_table = self.tournament_data.get_value("Min_At_Table")
        self.max_at_table = self.tournament_data.get_value("Max_At_Table")
        self.tournament_type_name = self.tournament_data.get_value("Type")
        self.set_type(self.tournament_type_name)
        #########################################################
        # zaladowanie graczy - tournament.players
        self.tournament_data.load_players(self.players)
        self.tournament_data.load_current_players(self.players,self.current_players)
        
        #########################################################
        # test do sprawdzenia czy gracze sie wczytali
        # for i in self.players.list:
        #     i.pt()
        # for i in self.current_players.list:
        #     i.pt()

    def create_tables():
        pass

    def end_round():
        pass

    def update_points(self):
        self.current_players.update_points()

    def end_swiss_round(self):
        self.update_points()
        self.current_players.swiss_sort()
        self.app.result("Swiss")
        self.save_players()
        self.save_curr_players()

    def end_single_elimination_round(self):
        self.current_players.single_elimination_sort()
        self.advancing_players, loosers = self.type.result(self.current_players)
        self.app.result("Single_Elimination")
        self.update_points()
        self.current_players = self.advancing_players
        self.save_players()
        self.save_curr_players()

    def get_players(self, players):
        if players == "current_players":
            return self.current_players.get_players()
        if players == "advancing_players":
            return self.advancing_players.get_players()
    
    def start_round_swiss(self):
        self.type.create_tables(self.current_players,self.tables)
        #########################################################
        # wyświetlić stoliki
        self.app.tables()

    def start_single_elimination_round(self):
        num_of_players = self.current_players.num_of_players()
        self.tables = self.next_tables.copy()
        num_at_tables = sum(self.tables)
        waiting = num_of_players - num_at_tables
        self.type.create_tables(self.current_players, self.tables)
        if len(self.tables) != 1 or waiting:
            self.next_tables = self.type.count_tables(num_of_players, self.min_at_table, self.max_at_table)
            advancing, ll = self.type.advancing_players(self.tables, self.next_tables, waiting)
        #########################################################
        # wyświetlić stoliki
        self.app.tables()
        if len(self.tables) == 1 and not waiting:
            self.app.last_round_information()
        else:
            #########################################################
            # advancing_players_information
            self.app.advancing_players_information(advancing, ll, waiting)

    def start_round(self):
        if type(self.type) == Swiss:
            self.start_round_swiss()

        if type(self.type) == Single_Elimination:
            self.start_single_elimination_round()


    def start_tournament(self, new):
        if new:
            self.current_players.copy(self.players)
        num = self.current_players.num_of_players()
        self.tables = self.type.count_tables(num, self.min_at_table, self.max_at_table, new_tournament=True)
        self.next_tables = self.tables.copy()

        self.start_round()

    def can_count_tables(self):
        num = self.players.num_of_players()
        print(num)
        tables = self.type.count_tables(num, self.min_at_table, self.max_at_table, new_tournament=True)
        print(tables)
        if tables:
            return True
        else:
            return False
