from PyQt5.QtWidgets import QLineEdit,QPushButton,QGridLayout,QWidget,QFileDialog,QMessageBox
from PyQt5.QtGui import QIntValidator


class Single_Elimination_Layout(QGridLayout):


    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        """
        #########################################################
        # Przyciski do wprowadzania ilosci rozgrywek w pojedynczej rundzie
        self.Game_Num = QLineEdit()
        self.Game_Num.setValidator(QIntValidator(1,20))
        self.Submit_Game_Num = QPushButton(self.main_window.get_text("Submit"))
        """
        #########################################################
        # Przyciski nastepna runda, zapisz i wyjdz
        self.Submit_Round = QPushButton(self.main_window.get_text("Next_Round"))
        self.Save_And_Exit = QPushButton(self.main_window.get_text("Save_And_Exit"))

        #########################################################
        # Layout
        self.Layout_Tables = QGridLayout()
        
        #########################################################
        # dodawanie graczy, stolow i okienek do wpisywania punktow
        self.add_players_and_tables()

    def submit_and_save(self):
        #########################################################
        # Przyciski nastepna runda, zapisz i wyjdz
        self.Submit_Round = QPushButton(self.main_window.get_text("Next_Round"))
        self.Save_And_Exit = QPushButton(self.main_window.get_text("Save_And_Exit"))

    def add_players_and_tables():
        pass

    """
    #########################################################
    # Funkcja do sprawedzania czy wpisano ilosc rozgrywek w rundzie
    def Game_Num(self):
        number = self.Game_Num.text()
        if not number:
            QMessageBox.warning(self.main_window, self.main_window.get_text("Error"), self.main_window.get_text("Specify_Value_For_Round"))
    """