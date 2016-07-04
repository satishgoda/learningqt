from PySide import QtCore
from PySide import QtGui

scene = QtGui.QGraphicsScene()

view = QtGui.QGraphicsView(scene)

view.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

view.show()

scene.addText("Hello, world!")

text1 = scene.items()[0]

text1.setVisible(False)

text1.setVisible(True)

brect  = text1.boundingRect()

text1rect = scene.addRect(brect)

text1rect.setVisible(False)

text1rect.setVisible(True)

text1.setPos(250, 0)

text1rect.setParentItem(text1)

text1.setPos(0, 0)

origin = scene.addEllipse(0, 0, 3, 3)

text1.setPos(100, 0)

text1.setVisible(False)

text1.setVisible(True)

text1.setPlainText("Hello Python Programmers")

brect = text1.boundingRect()

x, y, w, h = brect.x(), brect.y(), brect.width(), brect.height()

text1rect.setRect(brect)

text1.setPos(0, 0)

text1.setPos(100, 0)

text1rect.setParentItem(None)

text1.setPos(100, -100)

text1rect.setParentItem(text1)
