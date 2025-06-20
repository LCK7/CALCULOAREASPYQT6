import sys
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtWidgets import (QMainWindow,QLabel,QWidget,QVBoxLayout)
from src.vista.Tab_ui import crear_pestañas

class MainWindow(QMainWindow):
    """
    Ventana principal de la aplicación de cálculo de áreas.

    Esta clase configura la interfaz gráfica principal utilizando PyQt6,
    incluyendo un título, un conjunto de pestañas y un diseño estilizado.
    """
    
    def __init__(self):
        """
        Inicializa la ventana principal con un título, tamaño, 
        etiquetas y pestañas de contenido.
        """
        super().__init__()
        self.setWindowTitle("Aplicación de cálculo de Áreas")
        self.resize(QSize(600,500))
        
        label = QLabel("CALCULADORA DE ÁREAS")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        tabs = crear_pestañas()
        
        #Contenedor con layout vertical
        contenedor = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(tabs)
        contenedor.setLayout(layout)

        self.setCentralWidget(contenedor)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
            }
            QLabel {
                font-size: 24px;
                color: #f2f2ff;
                font-weight: bold;
                margin: 10px;                
            }          
        """)