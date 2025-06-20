import math
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton,QFormLayout
from src.logica.validators import PositiveDoubleValidator
from src.vista.results import ResultDisplay

class CirculoWidget(QWidget):
    """
    Widget para calcular el área de un círculo.

    Permite al usuario ingresar el radio, calcular el área y mostrar el resultado.
    Incluye validación para asegurar que el radio sea un número positivo.
    """
    def __init__(self):
        """
        Inicializa el widget de círculo.

        Args:
            grafico (optional): Parámetro opcional si se desea graficar el círculo.
        """
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        """
        Configura la interfaz del widget: campo de entrada, botones y display de resultado.
        """
        layout = QFormLayout(self)
        
        self.radio_input = QLineEdit()
        self.radio_input.setValidator(PositiveDoubleValidator())
        self.radio_input.setPlaceholderText("Ej: 3.5")
        self.radio_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #90caf9;
                border-radius: 6px;
                font-size: 14px;
                background-color: #2c2c2c;
                color: #ffffff;
            }
        """)

        self.calc_btn = QPushButton("Calcular")
        self.calc_btn.setStyleSheet("""
            QPushButton {
                background-color: #1e88e5;
                color: white;
                padding: 8px;
                margin: 5px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1565c0;
            }
        """)
        
        self.limpiar_btn = QPushButton("Limpiar")
        self.limpiar_btn.setStyleSheet("""
            QPushButton {
                background-color: #757575;
                color: white;
                margin: 5px;
                padding: 8px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #616161;
            }
        """)
        
        self.result_display = ResultDisplay()
        
        self.calc_btn.clicked.connect(self.calcular)
        self.limpiar_btn.clicked.connect(self.limpiar)

        layout.addRow("Radio:", self.radio_input)
        layout.addRow(self.limpiar_btn,self.calc_btn)
        layout.addRow(self.result_display)
        self.setStyleSheet("""
            QWidget {
                color: white;
                font-family: 'Segoe UI';
                font-size: 20px;
            }
        """)
        

    def calcular(self):
        """
        Realiza el cálculo del área del círculo usando el valor ingresado en el campo de texto.

        Si el valor no es válido, muestra un mensaje de error.
        """
        try:
            r = float(self.radio_input.text())
            area = math.pi * r**2
            self.result_display.set_result(area)
            
        except ValueError:
            self.result_display.show_error("Ingrese un radio válido")

    def limpiar(self):
        """
        Limpia los campos de entrada y resultado.
        """
        self.radio_input.clear()
        self.result_display.clear()
