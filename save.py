
import sys
import os
import time

from PyQt5.QtWidgets import *
    

class Window(QWidget):

    def parse(self):
        label = self.line_edit.text()
        label = label.lower()
        label = label.replace(" ", "_")
        label += '.py'
        self.parsed_label.setText(label)

    def save(self):
        os.system(f'mv ui.py saved/{self.parsed_label.text()}')
        f = open('saved/log', 'a')
        print(
            f"{self.parsed_label.text()}, {self.line_edit.text()}, "
            f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} \n"
        )
        f.write(f"{self.parsed_label.text()}, {self.line_edit.text()}, "
                f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} \n")
        f.close()
        self.close()

    def __init__(self):
        super().__init__()
        self.resize(600, 150)
        self.setWindowTitle("Salvează UI-ul generat anterior")
        layout = QFormLayout()
        self.line_edit = QLineEdit('')
        self.line_edit.setProperty("class", "save_line_edit")
        label_name = QLabel("Nume salvare:")
        label_name.setProperty("class", "label_name")
        layout.addRow(label_name, self.line_edit)
        self.parsed_label = QLabel()
        self.parsed_label.setProperty("class", "parsed_label")
        self.button = QPushButton("Salvează")
        self.button.setProperty("class", "save_button")
        self.button.clicked.connect(self.save)
        layout.addRow(self.button, self.parsed_label)
        self.line_edit.textChanged.connect(self.parse)
        self.setLayout(layout) 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
