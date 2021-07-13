
import sys
from PyQt5.QtWidgets import *
    

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QFormLayout()
        layout.addRow(QLabel("Inscriere in scoala"))
        layout.addRow("Nume:", QLineEdit())
        cb = QComboBox()
        cb.addItem("Scoala")
        cb.addItem("Liceu")
        cb.addItem("Facultate")
        layout.addRow("CNP:", QLineEdit())
        layout.addRow("Data nasterii:", QDateEdit())
        layout.addRow("Scoala:", QLineEdit())
        self.btn_inscrie = QPushButton("Inscrie-te acum!")
        layout.addWidget(self.btn_inscrie)
        self.btn_inscrie.clicked.connect(self.close)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
QPushButton { border: 2px solid green; border-radius: 10px; }
QPushButton:pressed { background-color: red; }
QWidget { background-color: green; }

The following code is a button with a red background and green text.

QPushButton {background-color: red; color: green;}""")
    window = Window()
    window.show()
    sys.exit(app.exec_())
