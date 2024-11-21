from PyQt5.QtWidgets import QMainWindow,QApplication
import sys

class MainWindow(QMainWindow):

    from CT_Window import ContinueTournament_Window, resize_ct,GetFile
    from NT_Window import NewTournament_Window,Min_on_submit,Max_on_submit, resize_nt, Add_player
    from init import initUI, resize_init, change_language, change_english_language, change_polish_language

    def __init__(self):
        super().__init__()
        self.initUI()

    #funkcja ktora jest wywolywana przy zmianie wielkosci okna
    def resizeEvent(self,event):
        if self.Mode == "INIT":
            self.resize_init() # zmiana wielkosci przyciskow przy zmianie rozmiaru okna w init

        elif self.Mode == "NT":
            self.resize_nt() #do zaimplementowania - zmiana wielkosci przyciskow przy zmianie rozmiaru okna
        
        elif self.Mode == "CT":
            self.resize_ct() #do zaimplementowania - zmiana wielkosci przyciskow przy zmianie rozmiaru okna

def main():    
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


a = main()
a.show()