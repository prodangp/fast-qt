
import sys
from PyQt5.QtWidgets import *
    

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QFormLayout()
        layout.addRow(QLabel("Inscriere la masterat"))
        layout.addRow("Nume:", QLineEdit())
        cb = QComboBox()
        cb.addItem("Facultatea")
        cb.addItem("Studiul")
        layout.addRow("Facultate:", cb)
        layout.addRow("Studii:", QLineEdit())
        self.btn_inscrie = QPushButton("Inscrie-te acum!")
        layout.addWidget(self.btn_inscrie)
        self.btn_inscrie.clicked.connect(self.close)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
QPushButton { color: red; background-color: white; }
QPushButton:pressed { background-color: green; }

The following code is an example of a button with a red background and green text.

QPushButton {background-color: red; color: green;}

The following code is an example of a button with a green background and bold text.

QPushButton {background-color: green; color: bold;}""")
    window = Window()
    window.show()
    sys.exit(app.exec_())
