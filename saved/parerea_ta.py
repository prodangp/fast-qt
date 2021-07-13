
import sys
from PyQt5.QtWidgets import *
    

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QFormLayout()
        layout.addRow(QLabel("Parerea ta despre conditiile de trafic"))
        layout.addRow("Nume:", QLineEdit())
        cb = QComboBox()
        cb.addItem("Nu am avut probleme")
        cb.addItem("Am avut probleme")
        layout.addRow("Conditiile de trafic:", cb)
        self.btn_parere = QPushButton("Parerea ta")
        layout.addWidget(self.btn_parere)
        self.btn_parere.clicked.connect(self.close)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""""")
    window = Window()
    window.show()
    sys.exit(app.exec_())
