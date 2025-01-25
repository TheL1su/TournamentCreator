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
            "Submit_Round" : "Zatwierdz Runde",
            "Save_And_Exit" : "Zapisz Turniej i wyjdź!",
            "Table" : "Stolik nr: ",
            "Table_And_Points" : "Stolik nr: 1          Duże punkty         Małe punkty",
            "Swiss" : "System Szwajcarski",
            "PlayOff" : "Play-off",
            "Points_Not_Filed" : "Uzupełnij brakujące punkty",
            "Advancing_Players_Information" : "Zasady awansu",
            "Places_From_Tables_That_Advance" : "Miejsca ktore w każdym stoliku awansują do nastepnej rundy:",
            "Lucky_Loosers" : "Liczba graczy awansująca z ",
            "Place" : " miejsca: ",
            "Waiting_In_Next_Round" : " graczy czekających awansuje do kolejnej kolejnej rundy.",
            "Next_Round" : "Nastepna runda",
            "Ranking" : "Ranking:",
            "Advancing" : "Awansujący:",
            "Eliminated" : "Wyeliminowani:",
            "Player" : "Gracz",
            "Big_Points" : "Duże Punkty",
            "Small_Points" : "Małe Punkty",
            "Waiting_Players" : "Gracze czekający w tej rundzie:",
            "Save_File" : "Zapisz plik",
            "Json_File" : "Plik json (*.json)",
            "Exit" : "Wyjscie",
            "Want_To_Exit" : "Czy napewno chcesz wyjsc?",
            "Path_Not_Selected" : "Sciezka nie wybrana!",
            "Start_Tournament" : "Rozpocznij Turniej",
            "Submit_And_Continue_Tournament" : "Zatwierdz i kontynuuj turniej",
            "Not_All_Values_Set" : "Nie wszystkie wartosci zostaly wprowadzone!"
        }
        
    def get_text(self,text):
        return self.dictionary[text]
    