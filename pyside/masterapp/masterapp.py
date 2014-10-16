import PySide
from PySide import QtGui, QtCore


class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, title, width=300, height=300):
        super(MyMainWindow, self).__init__()
        self.setWindowTitle(title)
        self.setFixedSize(width, height)
        self._initUI()

    def _initUI(self):
        self._widget = QtGui.QWidget()
        self.setCentralWidget(self._widget)
        self._layout = QtGui.QHBoxLayout()
        self._widget.setLayout(self._layout)
        self._button = QtGui.QPushButton("Close Window")
        self._tool1 = QtGui.QToolButton()
        self._layout.addWidget(self._button)
        self._layout.addWidget(self._tool1)
        self._button.clicked.connect(self.close)
        self._tool1.clicked.connect(self.close)

    def close(self):
        print("Closing")
        super(MyMainWindow, self).close()


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)

    window = MyMainWindow(title="Hello PySide", width=500, height=500)

    window.show()

    sys.exit(app.exec_())
