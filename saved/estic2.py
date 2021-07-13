
import sys
from PyQt5.QtWidgets import *
    

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QFormLayout()
        layout.addRow(QLabel("Concursul ESTIC"))
        layout.addRow("Nume:", QLineEdit())
        cb = QComboBox()
        cb.addItem("Elev")
        cb.addItem("Student")
        layout.addRow("Categorie:", cb)
        layout.addRow("Profesor coordonator:", QLineEdit())
        self.btn_inscrie = QPushButton("Inscrie-te!")
        layout.addWidget(self.btn_inscrie)
        self.btn_inscrie.clicked.connect(self.close)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
QLabel { color: blue; font-weight: bold; font-size: 12px; }
QWidget { background-color: yellow; }
QPushButton { min-height: 36px; max-width: 72px; border: 2px solid; border-radius: 18px; }
QPushButton:pressed { background-color: red; font-style: bold; }
QPushButton:disabled { background-color: yellow; color: blue; }""")
    window = Window()
    window.show()
    sys.exit(app.exec_())
