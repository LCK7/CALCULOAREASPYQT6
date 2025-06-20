import math
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton,QFormLayout
from src.logica.validators import PositiveDoubleValidator
from src.vista.results import ResultDisplay

class TrianguloWidget(QWidget):
    """
    Widget para calcular el área de un triángulo.

    Permite al usuario ingresar la base y la altura, calcular el área
    y mostrar el resultado. Incluye validación para asegurar que los valores
    ingresados sean positivos.
    """

    def __init__(self):
        """
        Inicializa el widget del triángulo y configura la interfaz gráfica.
        """
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        """
        Configura la interfaz del widget: campos de entrada, botones y display de resultado.
        """
        layout = QFormLayout(self)
        
        self.base_input = QLineEdit()
        self.base_input.setValidator(PositiveDoubleValidator())
        self.base_input.setPlaceholderText("Ej: 3.5")
        self.base_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #90caf9;
                border-radius: 6px;
                font-size: 14px;
                background-color: #2c2c2c;
                color: #ffffff;
            }
        """)
        self.altura_input = QLineEdit()
        self.altura_input.setValidator(PositiveDoubleValidator())
        self.altura_input.setPlaceholderText("Ej: 3.5")
        self.altura_input.setStyleSheet("""
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
                margin:5px;
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
                padding: 8px;
                margin:5px;
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

        layout.addRow("Base:", self.base_input)
        layout.addRow("Altura:", self.altura_input)
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
        Calcula el área del triángulo a partir de los valores ingresados.

        Si los valores son inválidos, muestra un mensaje de error.
        """
        try:
            base = float(self.base_input.text())
            altura = float(self.altura_input.text())
            area = base * altura / 2
            self.result_display.set_result(area)
        except ValueError:
            self.result_display.show_error("Ingrese un radio válido")

    def limpiar(self):
        """
        Limpia los campos de entrada y resultado.
        """
        self.base_input.clear()
        self.altura_input.clear()
        self.result_display.clear()