import PySide
from PySide import QtGui, QtCore

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)

    window = QtGui.QMainWindow()
    window.setWindowTitle("Hello PySide")
    window.setFixedSize(500, 500)

    widget = QtGui.QWidget()
    button = QtGui.QPushButton("Close Window", parent=widget)
    button.clicked.connect(window.close)

    window.setCentralWidget(widget)

    window.show()

    sys.exit(app.exec_())
