from collections import namedtuple

from PySide.QtGui import QWidget, QPalette, QPainter
from PySide.QtCore import Qt, QRect, QSize, Signal, Slot


ShapeType = namedtuple('ShapeType', 'Rectangle Circle Triangle')(*range(3))


class Shape(object):
    def __init__(self, type=ShapeType.Rectangle, color=Qt.red, rect=QRect()):
        self._type = type
        self._color = color
        self._rect = rect
        self._name = self.typeToString(type)

    @property
    def minSize(self):
        return QSize(80, 50)
    
    @classmethod
    def typeToString(cls, type):
        return ShapeType._fields[type] 
    
    @classmethod
    def stringToType(self, s, ok=0):
        return ShapeType._asdict()[s]

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
    currentShapeChanged = Signal(str)
    
    def __init__(self, parent=None):
        super(Document, self).__init__(parent)
        self._shapeList = []
        
        self.mousePressIndex = -1
        self.mousePressOffset = 0
        
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QPalette.Base)
        
        pal = QPalette()
        pal.setColor(QPalette.HighlightedText, Qt.red)
        self.setPalette(pal)

    def mouseMoveEvent(self, event):
        event.accept()
        
        shape = self._shapeList[self.mousePressIndex]
        rect  = shape.rect
        
        rect.moveTopLeft(event.pos() - self.mousePressOffset)
        
        size = rect.size().expandedTo(shape.minSize)
        rect.setSize(size)
        
        self.update()

    def mouseReleaseEvent(self, event):
        event.accept()
        self.mousePressIndex = -1

    def mousePressEvent(self, event):
        event.accept()
        
        for index, shape in enumerate(self._shapeList):
            if shape.rect.contains(event.pos()):
                self.mousePressIndex = index
                self.mousePressOffset = event.pos() - shape.rect.topLeft()
                print shape.name
                break

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
            
            # paint the shape name
            painter.setBrush(pal.text())
            painter.drawText(rect, Qt.AlignCenter, shape.name)

s1 = Shape(ShapeType.Rectangle, color=Qt.green, rect=QRect(0, 0, 100, 100))
s2 = Shape(ShapeType.Circle, rect=QRect(200, 200, 100, 100))

s3 = Shape(ShapeType.Circle, color=Qt.blue, rect=QRect(200, 200, 50, 50))
s4 = Shape(ShapeType.Rectangle, color=Qt.yellow, rect=QRect(0, 0, 25, 25))


d = Document()

d._shapeList = [s1, s2, s3, s4]

d.show()
