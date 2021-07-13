
import sys
from PyQt5.QtWidgets import *
    

class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QFormLayout()
        layout.addRow(QLabel("Exemplu de UI folosind stilul generat"))
        layout.addRow("Input de text:", QLineEdit())
        layout.addRow("Checkbox:", QCheckBox())
        layout.addRow("Combobox:", QComboBox())
        layout.addRow("Data:", QDateEdit())
        layout.addRow(QPushButton('Buton'))
        self.setLayout(layout) #end

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
QComboBox { background: gray; color: white; }
QPushButton { background: gray; color: white; } """)
    window = Window()
    window.show()
    sys.exit(app.exec_())
