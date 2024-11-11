from Language.Language_Interface import Language


class English(Language):
    def Title(self):
        return 'Welcome to Tournament Creator'
    
    def New_Tournament(self):
        return 'New Tournament'
    
    def Continue_Tournament(self):
        return 'Continue Tournament'