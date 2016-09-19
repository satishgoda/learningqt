import random

class ColoredButton(QtGui.QPushButton):
    def __init__(self, color, *args, **kwargs):
        super(ColoredButton, self).__init__(*args, **kwargs)

        self.color_ = color

        self.setFixedWidth(16)
        self.setFixedHeight(16)
        
        self.setCheckable(True)
        
        colorName = self.color_.name()

        self.setStyleSheet("""
        QPushButton {background-color: %s; color: black; border: none;}
        QPushButton:checked {background-color: %s; color: black; border: 1px solid grey;}
        """ % (colorName, colorName))
        
        self.setToolTip(self.color_.name())
        
        self.toggled.connect(self._onToggled)
        
    def _onToggled(self, checked):
        text = 'o' if checked else ''
        self.setText(text)

def getRandomQtColor():
    tuple4 = (random.randrange(0, 256) for _ in range(3))
    color = QtGui.QColor(*tuple4)
    return color

buttons = []

for index in range(1):
    randomColor = getRandomQtColor()
    self = ColoredButton(randomColor)
    self.show()
    buttons.append(self)
