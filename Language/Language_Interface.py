from abc import abstractmethod
#Interfejs dla Jezykow
class Language():

    @abstractmethod
    def getText(self,text):
        pass