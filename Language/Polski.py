from Language.Language_Interface import Language

class Polski(Language):
    def Title(self):
        return 'Witamy w Kreatorze Turniejów'
    
    def Choose_Language(self):
        return 'Język'

    def New_Tournament(self):
        return 'Nowy Turniej'
    
    def Continue_Tournament(self):
        return 'Kontynuuj Turniej'
    
    def Enter_Min_Players_At_Table(self):
        return 'Minimalna liczba graczy przy stoliku:'
    
    def Enter_Max_Players_At_Table(self):
        return 'Maksymalna liczba graczy przy stoliku:'
    
    def Submit(self):
        return 'Zatwierdź'
    
    def Error(self):
        return 'BŁĄÐ!'
    
    def Value(self):
        return 'Wprowadzona wartość'
    
    def Min_Bigger_Than_Max(self):
        return 'Minimalna wartość większa niż maksymalna!'

    def Max_Lower_Than_Min(self):
        return 'Maksymalna wartość mniejsza niż minimalna!'
    
    def Value_Not_Set(self):
        return 'Wartość nie ustawiona!'
    
    def Value_Set(self):
        return 'Ustawiona wartość: '

    def Choose_Tournament_Type(self):
        return 'Wybierz rodzaj Turnieju'
    
    def Enter_Player(self):
        return 'Wprowadź dane nowego gracza'
    
    def Browse(self):
        return 'Przeglądaj'
    
    def Title_Tournament_File(self):
        return 'Znajdz plik turnieju'