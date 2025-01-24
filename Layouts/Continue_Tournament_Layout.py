from PyQt5.QtWidgets import QLineEdit,QPushButton,QGridLayout,QWidget,QFileDialog,QMessageBox
from PyQt5.QtCore import QDir
from PyQt5.QtCore import Qt
import json
import os

class Continue_Tournament_Layout(QGridLayout):

    
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

            #########################################################
        # Przyciski do Kontynuowania Turnieju
        self.File_Input = QLineEdit()
        Label_Load_File = self.main_window.create_label("Load_File")
        self.Browse = QPushButton(self.main_window.get_text("Browse"))
        self.Browse.clicked.connect(self.GetFile)

        #########################################################
        # Przyciski do potwierdzenia wczytanego pliku i odpalenia turnieju
        self.Confirm = QPushButton(self.main_window.get_text("Submit_And_Continue_Tournament"))
        self.Confirm.adjustSize()
        self.Confirm.hide()
        self.Confirm.clicked.connect(self.OpenTournament)
        
        #########################################################
        # Dodawanie Przyciskow do Layoutu
        self.addWidget(Label_Load_File)
        self.addWidget(self.File_Input,1,0)
        self.addWidget(self.Browse,1,1)
        self.addWidget(self.Confirm,2,0)

        #########################################################
        # Layout przyciskow na siatce
        
        self.setAlignment(Label_Load_File, Qt.AlignBottom)
        self.setAlignment(self.File_Input, Qt.AlignTop)
        self.setAlignment(self.Browse,Qt.AlignTop)
        self.setAlignment(self.Confirm,Qt.AlignTop)


    def resize(self,width,height):
        """zmiana wielkosci przyciskow przy zmianie rozmiaru okna CT"""
        pass

    def GetFile(self):
        #########################################################
        # schowaj przycisk do zatwierdzania jezeli szukasz pliku
        self.Confirm.hide()

        #########################################################
        # Wybranie pliku z historia turnieju
        fileName, _ = QFileDialog.getOpenFileName(self.main_window, self.main_window.get_text("Title_Tournament_File"), QDir.rootPath() , '*.json')
        self.File_Input.setText(fileName)

        #########################################################
        # Funkcja otwierajaca plik
        self.OpenFile(fileName)

    def OpenFile(self,fileName):

        try:
            with open(fileName, 'r') as f:
                file_size = os.path.getsize(fileName) #rozmiar pliku

                if file_size==0: #pusty plik
                    self.main_window.show_warning(self.main_window.get_text("Error"), self.main_window.get_text("Empty_File"))

                else:
                    try: #probuje wczytac dane w formacie json

                        json_data = json.load(f)
                        #########################################
                        # Poprawne wczytanie pliku do slownika
                        self.main_window.tournament_data_update(json_data)
                        #########################################
                        # Pokazanie przycisku zatwierdz    
                        self.Show_Confirm_Button()

                    #############################################
                    # Blad w pliku
                    except json.JSONDecodeError as e:
                        self.main_window.show_warning(self.main_window.get_text("Error"),self.main_window.get_text("Syntax_Error"))

        #########################################################
        # Nie Wybrany plik
        except IOError as e:
            self.main_window.show_warning(self.main_window.get_text("Error"), self.main_window.get_text("File_Not_Selected"))

    def Show_Confirm_Button(self):
        self.Confirm.show()

    def OpenTournament(self):
        self.main_window.load_data()
        self.main_window.open_tournament(new=False)