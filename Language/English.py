from Language.Language_Interface import Language


class English(Language):
    def __init__(self):
        self.dictionary = {
            "Title" : "Welcome to Tournament Creator",
            "Choose_Language" : "Language",
            "New_Tournament" : "New Tournament",
            "Continue_Tournament" : "Continue Tournament",
            "Enter_Min_Players_At_Table" : "Minimal number of players at the table:",
            "Enter_Max_Players_At_Table" : "Maximal number of players at the table:",
            "Submit" : "Submit",
            "Error" : "ERROR",
            "Value" : "Value",
            "Min_Bigger_Than_Max" : "Minimal value bigger than maximal!",
            "Max_Lower_Than_Min" : "Maximal value lower than minimal!",
            "Value_Set" : "Value set: ",
            "Value_Not_Set" : "Value not set",
            "Choose_Tournament_Type" : "Choose Tournament Type",
            "Enter_Player" : "Enter new player data",
            "Browse" : "Browse",
            "Title_Tournament_File" : "Find tournament file",
            "File_Not_Selected" : "File not selected!",
            "Empty_File" : "Empty file!",
            "Syntax_Error" : "Data error in file!",
            "Load_File" : "Choose File that contains tournament data",
            "Specify_Value_For_Round" : "Specify number of games for this round!",
            "Next_Round" : "Next Round",
            "Save_And_Exit" : "Save Tournament and Exit!",
            "Table" : "Table nr: ",
            "Table_And_Points" : "Table nr: 1       Big points      Small Points",
            "Swiss" : "Swiss-system",
            "PlayOff" : "Play-off",
            "Points_Not_Filed" : "Fill missing points"
        }
        
    def get_text(self,text):
        return self.dictionary[text]