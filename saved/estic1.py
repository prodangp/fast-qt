
import sys
from PyQt5.QtWidgets import *
    

class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        layout.addRow(QLabel("Concursul ESTIC"))
        layout.addRow("Nume:", QLineEdit())
        layout.addRow("Prenume:", QLineEdit())
        layout.addRow("Adresa de e-mail:", QLineEdit())
        cb = QComboBox()
        cb.addItem("Elev")
        cb.addItem("Student")
        layout.addRow("Categorie:", cb)
        self.btn_inscrie = QPushButton("Inscrie-te acum!")
        layout.addWidget(self.btn_inscrie)
        self.btn_inscrie.clicked.connect(self.close)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""""")
    window = Window()
    window.show()
    sys.exit(app.exec_())
