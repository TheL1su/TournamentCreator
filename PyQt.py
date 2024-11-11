import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def on_click():
    print("Button clicked!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Moja aplikacja PyQt")
window.setGeometry(100, 100, 280, 80)

button = QPushButton("Kliknij mnie", window)
button.clicked.connect(on_click)
button.move(90, 30)

window.show()
sys.exit(app.exec_())




class Ulamek:
    def __init__(self,licznik,mianownik):
        self.mianownik = mianownik
        self.licznik = licznik
    def __mul__(self,obj):
        return Ulamek(self.licznik*obj.licznik, self.mianownik*obj.mianownik)


pierwszy =  Ulamek(1,2)
drugi = Ulamek(3,4)
trzeci = pierwszy * drugi
print(trzeci.mianownik,trzeci.licznik)