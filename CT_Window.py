from PyQt5.QtWidgets import QLineEdit,QPushButton,QGridLayout,QWidget,QFileDialog,QMessageBox
from PyQt5.QtCore import QDir
import json
import os


def ContinueTournament_Window(self):
    #########################################################
    # Zmiana Trybu
    self.Mode = "CT"

    #########################################################
    # Przyciski do Kontynuowania Turnieju
    self.File_Input = QLineEdit()
    self.Browse = QPushButton(self.Language.Browse())
    self.Browse.clicked.connect(self.GetFile)

    #########################################################
    # Przyciski do potwierdzenia wczytanego pliku i odpalenia turnieju
    self.Confirm = QPushButton(self.Language.Submit())
    self.Confirm.hide()
    
    #########################################################
    # Siatka dla Labeli i Przyciskow
    Layout_CT = QGridLayout()

    #########################################################
    # Dodawanie Przyciskow do Layoutu
    Layout_CT.addWidget(self.File_Input,0,0)
    Layout_CT.addWidget(self.Browse,0,1)
    Layout_CT.addWidget(self.Confirm,1,0)

    #########################################################
    # Usun stary i Wstaw nowy Widget Glowny
    self.Central_widget.deleteLater()
    self.Central_widget = QWidget(self)
    self.Central_widget.setLayout(Layout_CT)
    self.setCentralWidget(self.Central_widget)

def resize_ct(self):
    """zmiana wielkosci przyciskow przy zmianie rozmiaru okna CT"""
    pass

def GetFile(self):
    #########################################################
    # schowaj przycisk do zatwierdzania jezeli szukasz pliku
    self.Confirm.hide()

    #########################################################
    # Wybranie pliku z historia turnieju
    fileName, _ = QFileDialog.getOpenFileName(self, self.Language.Title_Tournament_File(), QDir.rootPath() , '*.json')
    self.File_Input.setText(fileName)

    #########################################################
    # Funkcja otwierajaca plik
    self.OpenFile(fileName)

def OpenFile(self,fileName):

    try:
        with open(fileName, 'r') as f:
            file_size = os.path.getsize(fileName) #rozmiar pliku

            if file_size==0: #pusty plik
                QMessageBox.warning(self, self.Language.Error(), self.Language.Empty_File())

            else:
                try: #probuje wczytac dane w formacie json

                    json_data = json.load(f)
                    #########################################
                    # Poprawne wczytanie pliku do slownika
                    self.TournamentDict.update(json_data)
                    #########################################
                    # Stworzenie przycisku zatwierdz    
                    self.Show_Confirm_Button()

                #############################################
                # Blad w pliku
                except json.JSONDecodeError as e:
                    QMessageBox.warning(self, self.Language.Error(), self.Language.Syntax_Error())

    #########################################################
    # Nie Wybrany plik
    except IOError as e:
        QMessageBox.warning(self, self.Language.Error(), self.Language.File_Not_Selected())

    #########################################################
    # NIE WIEM CZY IMPLEMENTOWAC
    #except: #handle other exceptions such as attribute errors
    #    print("Unexpected error:", sys.exc_info()[0]) 
    #    print("done")

def Show_Confirm_Button(self):
    self.Confirm.show()
    