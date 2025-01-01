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
            "Value_set" : "Value set: ",
            "Value_Not_Set" : "Value not set",
            "Choose_Tournament_Type" : "Choose Tournament Type",
            "Enter_Player" : "Enter new player data",
            "Browse" : "Browse",
            "Title_Tournament_File" : "Find tournament file",
            "File_Not_Selected" : "File not selected!",
            "Empty_File" : "Empty file!",
            "Syntax_Error" : "Data error in file!",
            "Load_File" : "Choose File that contains tournament data"

        }
        
    def getText(self,text):
        return self.dictionary[text]