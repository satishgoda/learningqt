
from PySide import QtCore
from PySide import QtGui


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
    
    @property
    def lay(self):
        return self.layout()

self = MyWidget()

self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

self.show()

self.setLayout(QtGui.QHBoxLayout())

self.lay.addWidget(QtGui.QPushButton('1'))
self.lay.itemAt(0).widget().adjustSize()

self.lay.addStretch()

self.lay.setAlignment(QtCore.Qt.AlignTop)

self.lay.update()

self.lay.itemAt(self.lay.count()-1)

self.lay.takeAt(self.lay.count()-1)

self.lay.addSpacing(20)

si = self.lay.itemAt(self.lay.count()-1)

si.sizeHint()

si.changeSize(50, 0)

self.lay.update()

self.lay.addStretch()

self.lay.addWidget(QtGui.QPushButton('2'))

si.changeSize(0, 0)

self.lay.update()

si.changeSize(50, 0)

self.lay.update()

self.lay.contentsMargins()

self.lay.setContentsMargins(1, 1, 1, 1)

si.changeSize(0, 0)

self.lay.update()

self.lay.setContentsMargins(0, 0, 0, 0)

self.lay.setSpacing(0)

self.lay.update()
