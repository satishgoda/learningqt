
from PySide import QtCore
from PySide import QtGui

class MyHBoxLayout(QtGui.QHBoxLayout):
    def __init__(self, *args, **kwargs):
        super(MyHBoxLayout, self).__init__(*args, **kwargs)
    
    @property
    def margins(self):
        return self.contentsMargins()
    
    @margins.setter
    def margins(self, margins):
        self.setContentsMargins(*margins)

class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.setLayout(MyHBoxLayout())
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    
    @property
    def lay(self):
        return self.layout()

self = MyWidget()

self.show()

##

self.lay.addWidget(QtGui.QPushButton('1'))

self.lay.addWidget(QtGui.QPushButton('2'))

self.lay.margins = [0] * 4

self.lay.setSpacing(15)

self.lay.addStretch()

self.lay.addWidget(QtGui.QPushButton('3'))

self.lay.setSpacing(0)

self.lay.setSpacing(10)
