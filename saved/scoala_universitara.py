
import sys
from PyQt5.QtWidgets import *
    

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QFormLayout()
        layout.addRow(QLabel("Inscrierea in scoala"))
        layout.addRow("Nume:", QLineEdit())
        cb = QComboBox()
        cb.addItem("Scoala preuniversitara")
        cb.addItem("Universitate")
        layout.addRow("Scoala:", cb)
        layout.addRow("Data nasterii:", QDateEdit())
        layout.addRow("CNP:", QLineEdit())
        self.btn_inscrie = QPushButton("Inscrie-te")
        layout.addWidget(self.btn_inscrie)
        self.btn_inscrie.clicked.connect(self.close)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
QWidget { background-color: green; }
QPushButton { border: 2px solid red; border-radius: 18px; }
QPushButton:pressed { background-color: red; }
QPushButton:hover { background-color: green; }
QPushButton:hover:pressed { background-color: red; }

The following code is a simple example of a button with a red background and green text.

QPushButton {background-color: red; color: green;}
""")
    window = Window()
    window.show()
    sys.exit(app.exec_())
