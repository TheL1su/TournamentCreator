

class Tournament_Data:
    def __init__(self):
        self.tournament_data = {}

    #########################################################
    # Funkcja sprawdzajaca czy klucz istnieje w slowniku 
    def key_check(self,key):
        if key in self.tournament_data:
            return True
        else:
            return False
        

    #########################################################
    # Funkcja zwracajaca wartosc dla klucza
    def get_value(self,key):
        return self.tournament_data.get(key)
    
    #########################################################
    # Funkcja wykonujaca update na slowniku
    def update(self,dictionary):
        self.tournament_data.update(dictionary)