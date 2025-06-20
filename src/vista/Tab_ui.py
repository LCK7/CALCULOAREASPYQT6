import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTabWidget
from src.vista.widgets.cuadrado_widget import CuadradoWidget
from src.vista.widgets.circulo_widget import CirculoWidget
from src.vista.widgets.rectangulo_widget import RectanguloWidget
from src.vista.widgets.triangulo_widget import TrianguloWidget

def crear_pestañas():
    """
    Crea un widget de pestañas con diferentes figuras geométricas.

    Returns:
        QTabWidget: Widget que contiene las pestañas para calcular áreas
        de círculo, cuadrado, rectángulo y triángulo.
    """
    
    tab = QTabWidget()
    tab.addTab(CirculoWidget(), "Círculo")
    tab.addTab(CuadradoWidget(), "Cuadrado")
    tab.addTab(RectanguloWidget(), "Rectángulo")
    tab.addTab(TrianguloWidget(), "Triángulo")
    tab.setStyleSheet("""
        QTabWidget {
            background-color: #2a2a2a;      
            color: #000000;
            padding: 30px;
        }
        QTabBar::tab {
            background:  #90caf9;
            color: #000000;
            padding: 8px;
            margin: 3px;
            border-radius: 2px;
            font: 14px;
        }
        QTabBar::tab:hover {
            background: #42a5f5;
        }
        QTabBar::tab:selected {
            background: #1E88E5;
        }
    """)
    return tab
