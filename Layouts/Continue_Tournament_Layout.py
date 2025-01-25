from PyQt5.QtWidgets import QLineEdit,QPushButton,QGridLayout,QWidget,QFileDialog,QMessageBox,QVBoxLayout
from PyQt5.QtCore import QDir
from PyQt5.QtCore import Qt
import json
import os

class Continue_Tournament_Layout(QVBoxLayout):

    
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

            #########################################################
        # Przyciski do Kontynuowania Turnieju
        self.File_Input = self.main_window.create_line_edit()
        self.File_Input.setFixedWidth(self.main_window.width())
        Label_Load_File = self.main_window.create_bold_label("Load_File")
        self.Browse = self.main_window.create_push_button("Browse")
        self.Browse.clicked.connect(self.GetFile)

        #########################################################
        # Przyciski do potwierdzenia wczytanego pliku i odpalenia turnieju
        self.Confirm = self.main_window.create_push_button("Submit_And_Continue_Tournament")
        self.Confirm.adjustSize()
        self.Confirm.hide()
        self.Confirm.clicked.connect(self.OpenTournament)
        
        #########################################################
        # Dodawanie Przyciskow do Layoutu
        self.addStretch()
        self.addWidget(Label_Load_File)
        self.addSpacing(10)
        self.addWidget(self.File_Input)
        self.addSpacing(10)
        self.addWidget(self.Browse)
        self.addSpacing(200)
        self.addWidget(self.Confirm)
        self.addStretch()
        #########################################################
        # Layout przyciskow na siatce
        
        self.setAlignment(Label_Load_File, Qt.AlignCenter)
        self.setAlignment(self.File_Input, Qt.AlignCenter)
        self.setAlignment(self.Browse,Qt.AlignCenter)
        self.setAlignment(self.Confirm,Qt.AlignCenter)


    def resize(self,width,height):
        """zmiana wielkosci przyciskow przy zmianie rozmiaru okna CT"""
        self.File_Input.setFixedWidth(width//2)
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