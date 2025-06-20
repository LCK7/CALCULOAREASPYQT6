from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt

class ResultDisplay(QLabel):
    """
    Widget personalizado para mostrar resultados y errores relacionados
    con el cálculo de áreas.
    """
    
    def __init__(self):
        """
        Inicializa el widget de resultado con un texto por defecto y
        alineación centrada horizontalmente.
        """
        super().__init__("Área: ")
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
    def set_result(self, value):
        """
        Muestra el resultado del cálculo formateado con dos decimales.

        Args:
            value (float): Resultado del área a mostrar.
        """
        self.setText(f"Área: {value:.2f}")
    
    def show_error(self, message):
        """
        Muestra un mensaje de error en lugar del resultado.

        Args:
            message (str): Texto del mensaje de error.
        """
        self.setText(f"Error: {message}")
    
    def clear(self):
        """
        Restaura el texto original del widget.
        """
        self.setText("Área: ")