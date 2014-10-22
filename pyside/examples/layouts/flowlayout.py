#!/usr/bin/env python

"""PyQt4 port of the layouts/flowlayout example from Qt v4.x"""
# https://qt.gitorious.org/pyside/pyside-examples/source/07c17233c1d3cb0f7a4b6e0bbfcc641ef4b4f5a4:examples/layouts/flowlayout.py

from PySide import QtCore, QtGui


class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        layout = QtGui.QVBoxLayout()
        self.le = QtGui.QLineEdit(self)
        self.le.setObjectName('search')
        layout.addWidget(self.le)

        self.le.textEdited.connect(self.update)

        flowLayout = FlowLayout()

        for char in map(chr, range(65, 65+26)):
            pb = QtGui.QPushButton(char)
            pb.setObjectName(char)
            flowLayout.addWidget(pb)

        layout.addLayout(flowLayout)

        self.setLayout(layout)

        self.setWindowTitle("Flow Layout")

    def update(self):
        print "Updated ", self.le.text()

class FlowLayout(QtGui.QLayout):
    def __init__(self, parent=None, margin=0, spacing=-1):
        super(FlowLayout, self).__init__(parent)

        if parent is not None:
            self.setContentsMargins(margin, margin, margin, margin)

        self.setSpacing(spacing)

        self.itemList = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]

        return None

    def takeAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)

        return None

    def expandingDirections(self):
        return QtCore.Qt.Orientations(QtCore.Qt.Orientation(0))

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self.doLayout(QtCore.QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QtCore.QSize()

        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        a, b = self.getContentsMargins()[0:2]
        size += QtCore.QSize(2*a, 2*b)
        return size

    def doLayout(self, rect, testOnly):
        x = rect.x()
        y = rect.y()
        lineHeight = 0

        for item in self.itemList:
            wid = item.widget()
            spaceX = self.spacing() + wid.style().layoutSpacing(QtGui.QSizePolicy.PushButton, QtGui.QSizePolicy.PushButton, QtCore.Qt.Horizontal)
            spaceY = self.spacing() + wid.style().layoutSpacing(QtGui.QSizePolicy.PushButton, QtGui.QSizePolicy.PushButton, QtCore.Qt.Vertical)
            nextX = x + item.sizeHint().width() + spaceX
            if nextX - spaceX > rect.right() and lineHeight > 0:
                x = rect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
                item.setGeometry(QtCore.QRect(QtCore.QPoint(x, y), item.sizeHint()))

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y()


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = Window()
    mainWin.show()
    sys.exit(app.exec_())
