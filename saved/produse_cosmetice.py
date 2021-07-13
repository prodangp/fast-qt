
import sys
from PyQt5.QtWidgets import *
    

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QFormLayout()
        layout.addRow(QLabel("Cosmetice"))
        layout.addRow("Nume:", QLineEdit())
        cb = QComboBox()
        cb.addItem("Cosmetice")
        layout.addRow("Produse:", cb)
        self.btn_cumpara = QPushButton("Cumpara acum")
        layout.addWidget(self.btn_cumpara)
        self.btn_cumpara.clicked.connect(self.close)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
QWidget { background-color: blue; }
QPushButton:pressed { background-color: red; }
QPushButton { border-width: 2px; border-style: solid; border-radius: 10px; }
QLineEdit { background-color: yellow; }
QPushButton { min-height: 36px; max-width: 72px; border: 2px solid; border-radius: 18px; }
QLineEdit { background-color: yellow; }

The following code shows the result of the example above.""")
    window = Window()
    window.show()
    sys.exit(app.exec_())
