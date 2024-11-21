from PyQt5.QtWidgets import QLineEdit,QPushButton,QGridLayout,QWidget,QFileDialog
from PyQt5.QtCore import QDir

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
    # Siatka dla Labeli i Przyciskow
    Layout_CT = QGridLayout()

    #########################################################
    # Dodawanie Przyciskow do Layoutu
    Layout_CT.addWidget(self.File_Input,0,0)
    Layout_CT.addWidget(self.Browse,0,1)

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
    fileName, _ = QFileDialog.getOpenFileName(self, self.Language.Title_Tournament_File(), QDir.rootPath() , '*.json')
    self.File_Input.setText(fileName)
