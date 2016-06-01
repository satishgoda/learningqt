##

from PySide import QtCore
from PySide import QtGui


##

class MyScene(QtGui.QGraphicsScene):
    def __init__(self, parent=None):
        super(MyScene, self).__init__(parent)
    
    def mousePressEvent(self, mouseEvent):
        if mouseEvent.button() != QtCore.Qt.LeftButton:
            return
        
        print "Left mouse button pressed"
        
    def mouseReleaseEvent(self, mouseEvent):
        if mouseEvent.button() != QtCore.Qt.LeftButton:
            return
        
        print "Left mouse button was released"
        
        item = self.items()[0]
        item.setPos(mouseEvent.scenePos())

class MyView(QtGui.QGraphicsView):
    def __init__(self, scene, parent=None):
        super(MyView, self).__init__(scene, parent)
##

scene = MyScene()

##

view = MyView(scene)

##

view.show()

##

scene.addText("Hello")
##

len(scene.items())
