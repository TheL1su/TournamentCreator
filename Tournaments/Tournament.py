from Tournaments.Player import Player,Players
from Tournaments.Types.Swiss import Swiss
from Tournaments.Types.Single_Elimination import Single_Elimination


class Tournament:

    def __init__(self,app):
        self.app = app
        self.players = Players()
        self.current_players = Players()
        self.min_at_table = -1
        self.max_at_table = -1
        self.tables = []
        self.prev_tables = []
        self.ready_to_calculate = False

    def add_player(self,player):
        name = player.split(" ")[0]
        surname = player.split(" ")[1]
        self.players.add_player(Player(name,surname))

    def add_type(self,tournament_type):
        if tournament_type == "Swiss":
            self.type = Swiss()
            self.tournament_type_name = "Swiss"
        elif tournament_type == "Single_Elimination":
            self.type = Single_Elimination()
            self.tournament_type_name = "Single_Elimination"


    def get_min_at_table(self):
        return self.min_at_table
    
    def get_max_at_table(self):
        return self.max_at_table

    def set_min_at_table(self,number):
        self.min_at_table = number

    def set_max_at_table(self,number):
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
        self.current_players.big_points_change(self,player_cnt,num)

    #########################################################
    # Funkcja zmieniajaca male punkty zawodnikowi
    def small_points_change(self,player_cnt,num):
        self.current_players.small_points_change(self,player_cnt,num)

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
        self.ready_to_calculate = True
    
    def get_type(self):
        return self.tournament_type_name

    #########################################################
    # Funkcja odpowiadajaca za rozpoczecie i zarzadzanie turniejem
    def manage(self):
        #########################################################
        # Odpal layout turnieju
        self.app.tournament_layout()

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

        pass

    def load_data():
        pass

    def create_tables():
        pass

    def end_round():
        pass

    def update_data():
        pass