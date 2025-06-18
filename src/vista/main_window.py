import sys
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicacion de calculo de Areas")
        self.setFixedSize(QSize(400,300))
        
        label = QLabel("CALCULADORA DE AREAS")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setCentralWidget(label)
        
        menubar = QMenuBar("Barra de Tareas")
        self.addMenuBar(menubar)
        
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()