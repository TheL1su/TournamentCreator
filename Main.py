from PyQt5.QtWidgets import QMainWindow,QApplication
import sys
from Application import Application


def main():    
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())


a = main()
a.show()