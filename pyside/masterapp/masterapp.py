import PySide
from PySide import QtGui, QtCore


class MyMainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self._initUI()

    def _initUI(self):
        self._widget = QtGui.QWidget()
        self.setCentralWidget(self._widget)
        self._button = QtGui.QPushButton("Close Window", parent=self._widget)
        self._button.clicked.connect(self.close)

    def close(self):
        print("Closing")
        super(MyMainWindow, self).close()


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)

    window = MyMainWindow()
    window.setWindowTitle("Hello PySide")
    window.setFixedSize(500, 500)

    window.show()

    sys.exit(app.exec_())
