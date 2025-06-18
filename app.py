import sys
from PyQt6.QtWidgets import QApplication
from src.vista.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()

    app.exec()
    