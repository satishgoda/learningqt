from collections import namedtuple

from PySide.QtGui import QWidget, QPalette, QPainter
from PySide.QtCore import Qt, QRect


ShapeType = namedtuple('ShapeType', 'Rectangle Circle Triangle')(*range(3))


class Shape(object):
    def __init__(self, type=ShapeType.Rectangle, color=Qt.red, rect=QRect()):
        self._type = type
        self._color = color
        self._rect = rect

    @property
    def type(self):
        return self._type
    
    @property
    def color(self):
        return self._color
    
    @property
    def rect(self):
        return self._rect
    
    @property
    def name(self):
        return self._name
        

class Document(QWidget):
    def __init__(self, parent=None):
        super(Document, self).__init__(parent)
        self._shapeList = []
        
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QPalette.Base)
        
        pal = QPalette()
        pal.setColor(QPalette.HighlightedText, Qt.red)
        self.setPalette(pal)

    def paintEvent(self, event):
        paintRegion = event.region()
        painter = QPainter(self)
        pal = self.palette()

        for shape in self._shapeList:
            rect = shape.rect
            
            if not paintRegion.contains(rect):
                continue
            
            shapeType = shape.type
            
            painter.setBrush(shape.color)
            
            if shapeType == ShapeType.Rectangle:
                print "rectangle"
                painter.drawRect(rect)
            elif shapeType == ShapeType.Circle:
                print "circle"
                painter.drawEllipse(rect)

s1 = Shape(ShapeType.Rectangle, color=Qt.green, rect=QRect(0, 0, 100, 100))
s2 = Shape(ShapeType.Circle, rect=QRect(200, 200, 100, 100))

d = Document()

d._shapeList = [s1, s2]

d.show()
