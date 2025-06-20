from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtCore import QLocale

class PositiveDoubleValidator(QDoubleValidator):
    """
    Validador para asegurarse de que el número ingresado sea un decimal positivo.

    Configura el QDoubleValidator para aceptar solo valores mayores a 0,
    con hasta 2 decimales y con la configuración regional en español.
    """
    def __init__(self):
        """
        Inicializa el validador con límites positivos y formato decimal regional.
        """
        super().__init__()
        self.setBottom(0.01)  # Valores > 0
        self.setDecimals(2)   # Máximo 2 decimales