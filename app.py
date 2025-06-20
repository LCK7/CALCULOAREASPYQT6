import sys
from PyQt6.QtWidgets import QApplication
from src.vista.main_window import MainWindow

def main():

    """
    Punto de entrada principal de la aplicación Calculadora de Áreas.

    Crea una instancia de QApplication, muestra la ventana principal
    y ejecuta el bucle principal del evento.
    """

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
        main()