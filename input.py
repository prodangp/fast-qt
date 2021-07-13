

class Input:
    def __init__(self):
        self._pyqt: str = ''
        self._qss: str = ''

    def set_pyqt(self, text):
        self._pyqt = text

    def set_qss(self, text):
        self._qss = text

    def get_pyqt(self):
        return self._pyqt

    def get_qss(self):
        return self._qss