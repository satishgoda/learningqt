##

from PySide import QtCore
from PySide import QtGui

##


scene = QtGui.QGraphicsScene()

view = QtGui.QGraphicsView(scene)

view.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

##

view.show()

##

scene.addText("Hello, world!")

##

scene.setBackgroundBrush(QtCore.Qt.cyan)

##

scene.addEllipse(50, 0, 50, 50)

##

ellipse, text = scene.items()

ellipse.setPos(0, 0)

text.setPos(0, 0)

## 

scene.views()[0] is view

scene.itemsBoundingRect()

brush = QtGui.QBrush(QtCore.Qt.lightGray, QtCore.Qt.CrossPattern)

scene.setForegroundBrush(brush)

view.rotate(-45)
