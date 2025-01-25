from PyQt5.QtWidgets import QGridLayout,QLabel,QLineEdit,QPushButton,QMessageBox,QWidget,QToolButton,QMenu,QAction


########################################
# Klasa do tworzenia widgetow
class WidgetsFactory:
    def __init__(self) -> None:
        pass

    def create_tool_button(self, *, parent, text, menu):
        """Metoda tworzy przycisk do rozwijania menu"""
        button = QToolButton(parent = parent)
        button.setText(text)
        button.setMenu(menu)
        button.setPopupMode(QToolButton.InstantPopup)  # Ustawienie, aby Menu rozwijało się natychmiast
        button.setStyleSheet("color: black; border-radius: 8px;background-color: #4CAF50; font-family: Arial; font-size: 18pt")
        return button

    def create_label(self, text):
        """Metoda tworzy etykiete"""
        label = QLabel(text)
        label.setStyleSheet('color: white;font-weight: normal; font-size: 18pt')
        return label
    
    def create_bold_label(self, text):
        """Metoda tworzy etykiete"""
        label = QLabel(text)
        label.setStyleSheet('color: white;font-weight: bold; font-size: 18pt')
        return label