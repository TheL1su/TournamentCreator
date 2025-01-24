from PyQt5.QtWidgets import QMessageBox

class MessageBoxFactory:
    @staticmethod
    def show_information(parent, title, message):
        QMessageBox.information(parent, title, message)

    @staticmethod
    def show_warning(parent, title, message):
        QMessageBox.warning(parent, title, message)

    @staticmethod
    def show_question(parent, title, message):
        response = QMessageBox.question(parent, title, message, QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            return True
        else:
            return False

    @staticmethod
    def show_critical(parent, title, message):
        QMessageBox.critical(parent, title, message)