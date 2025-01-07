from Language.Language_Interface import Language

class Polski(Language):

    def __init__(self):
        self.dictionary = {
            "Title" : "Witamy w Kreatorze Turniejów",
            "Choose_Language" : "Język",
            "New_Tournament" : "Nowy Turniej",
            "Continue_Tournament" : "Kontynuuj Turniej",
            "Enter_Min_Players_At_Table" : "Minimalna liczba graczy przy stoliku:",
            "Enter_Max_Players_At_Table" : "Maksymalna liczba graczy przy stoliku:",
            "Submit" : "Zatwierdź",
            "Error" : "BŁĄÐ!",
            "Value" : "Wprowadzona wartość",
            "Min_Bigger_Than_Max" : "Minimalna wartość większa niż maksymalna!",
            "Max_Lower_Than_Min" : "Maksymalna wartość mniejsza niż minimalna!",
            "Value_Set" : "Ustawiona wartość: ",
            "Value_Not_Set" : "Wartość nie ustawiona!",
            "Choose_Tournament_Type" : "Wybierz rodzaj Turnieju",
            "Enter_Player" : "Wprowadź dane nowego gracza",
            "Browse" : "Przeglądaj",
            "Title_Tournament_File" : "Znajdz plik turnieju",
            "File_Not_Selected" : "Nie wybrano pliku!",
            "Empty_File" : "Pusty plik!",
            "Syntax_Error" : "Dane w pliku zawieraja blad!",
            "Load_File" : "Wybierz plik ktory zawiera dane turnieju",
            "Specify_Value_For_Round" : "Okresl ilosc rozgrywek w tej rundzie!",
            "Next_Round" : "Nastepna Runda",
            "Save_And_Exit" : "Zapisz Turniej i wyjdź!",
            "Table" : "Stolik nr: ",
            "Table_And_Points" : "Stolik nr: 1      Duże punkty     Małe punkty",
            "Swiss" : "System Szwajcarski",
            "PlayOff" : "Play-off",
            "Points_Not_Filed" : "Uzupełnij brakujące punkty"
        }
        
    def get_text(self,text):
        return self.dictionary[text]
    