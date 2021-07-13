from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from mainwindow import UiMainWindow

from GPT3 import GPT3


class GUI(QMainWindow, UiMainWindow):
    """ Aceasta este principala clasă GUI. Este responsabilă pentru fluxul aplicației și controlul widgeturilor,
        împreună cu crearea conexiuni și semnale pentru a declanșa diferite funcționalități. Aproximativ toate
        componentele grafice sunt definite în clasa părinte: class: `UiMainWindow`."""

    def __init__(self):
        """Constructor method
        """
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.btn_create.clicked.connect(lambda: self.create_ui())
        print('############# GPT-3 PyQt5 Creator GUI #############')

    def create_ui(self):
        gpt3 = GPT3()
        if self.ck_pyqt.isChecked():
            if self.ck_qss.isChecked():
                gpt3.select_shots('qss')
                gpt3.generate_style(self.input_.get_qss())
            gpt3.select_shots('pyqt')
            gpt3.generate_ui(self.input_.get_pyqt())
        else:
            if self.ck_qss.isChecked():
                gpt3.select_shots('qss')
                gpt3.generate_style(self.input_.get_qss())
                gpt3.generate_placeholder()
            else:
                self.error_dialog = QtWidgets.QErrorMessage()
                self.error_dialog.showMessage('Trebuie să selectezi codul ce va fi generat (PyQt5/QSS).')
                return

        self.btn_save.setEnabled(True)
        self.btn_clear.setEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open('manjaro.qss').read())
    ui = GUI()
    ui.show()
    sys.exit(app.exec_())
