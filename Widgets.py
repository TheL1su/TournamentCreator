from PyQt5.QtWidgets import QGridLayout,QLabel,QLineEdit,QPushButton,QMessageBox,QWidget,QToolButton,QMenu,QAction


########################################
# Klasa do tworzenia widgetow
class WidgetsFactory:
    def __init__(self) -> None:
        self.font_size = "font-size: 16pt;"
        self.padding = "padding: 10px 20px;"
        pass

    def create_tool_button(self, *, parent, text, menu):
        """Metoda tworzy przycisk do rozwijania menu"""
        button = QToolButton(parent = parent)
        button.setText(text)
        button.setMenu(menu)
        button.setPopupMode(QToolButton.InstantPopup)  # Ustawienie, aby Menu rozwijało się natychmiast
        button.setStyleSheet("color: black; border-radius: 8px;background-color: #4CAF50; font-family: Arial;"+self.font_size+self.padding)
        return button

    def create_label(self, text):
        """Metoda tworzy etykiete"""
        label = QLabel(text)
        label.setStyleSheet("color: white;font-weight: normal;"+self.font_size)
        return label
    
    def create_bold_label(self, text):
        """Metoda tworzy etykiete"""
        label = QLabel(text)
        label.setStyleSheet('color: white;font-weight: bold;'+self.font_size)
        return label
    
    def create_line_edit(self):
        lineedit = QLineEdit()
        lineedit.setStyleSheet('font-weight: normal;'+self.font_size)
        return lineedit

    def create_push_button(self, text):
        pushbutton = QPushButton(text)
        pushbutton.setStyleSheet('font-weight: normal;'+self.font_size+self.padding)
        return pushbutton
