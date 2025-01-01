from abc import abstractmethod
#Interfejs dla Jezykow
class Language:

    @abstractmethod
    def get_text(self,text):
        pass