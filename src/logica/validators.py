from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtCore import QLocale

class PositiveDoubleValidator(QDoubleValidator):
    def __init__(self):
        super().__init__()
        self.setBottom(0.01)  # Valores > 0
        self.setDecimals(2)   # Máximo 2 decimales
        self.setLocale(QLocale('es')) #Configuración reginal española