from Language.Language_Interface import Language


class English(Language):
    def Title(self):
        return 'Welcome to Tournament Creator'
    
    def Choose_Language(self):
        return 'Language'

    def New_Tournament(self):
        return 'New Tournament'
    
    def Continue_Tournament(self):
        return 'Continue Tournament'
    
    def Enter_Min_Players_At_Table(self):
        return 'Minimal number of players at the table:'
    
    def Enter_Max_Players_At_Table(self):
        return 'Maximal number of players at the table:'
    
    def Submit(self):
        return 'Submit'
    
    def Error(self):
        return 'ERROR'
    
    def Value(self):
        return 'Value set'
    
    def Min_Bigger_Than_Max(self):
        return 'Minimal value bigger than maximal!'
    
    def Max_Lower_Than_Min(self):
        return 'Maximal value lower than minimal!'
    
    def Value_Set(self):
        return 'Value set:'

    def Value_Not_Set(self):
        return 'Value not set'
    
    def Choose_Tournament_Type(self):
        return 'Choose_Tournament_Type'