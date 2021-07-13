
import sys
from PyQt5.QtWidgets import *
    

class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QFormLayout()
        layout.addRow("Bilet", QLabel())
        layout.addRow("Nume:", QLineEdit())
        layout.addRow("Data:", QLineEdit())
        layout.addRow("Cota:", QLineEdit())
        layout.addRow("Categorie:", QLineEdit())
        #layout.addRow("Numar pliculete:", QLineEdit())
        self.setLayout(layout)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""""")
    window = Window()
    window.show()
    sys.exit(app.exec_())
