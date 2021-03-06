
class ColoredButtonGroup(QtGui.QGroupBox):
    def __init__(self, numColBut, *args, **kwargs):
        super(ColoredButtonGroup, self).__init__(*args, **kwargs)
        self.numColBut = numColBut

        self.buttonGroup = QtGui.QButtonGroup()
        
        layout = QtGui.QHBoxLayout()
        layout.setSpacing(1)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSizeConstraint(SetFixedSize)
        
        self.setLayout(layout)
        
        for _ in range(self.numColBut):
            randomColor = getRandomQtColor()
            button = ColoredButton(randomColor)
            self.buttonGroup.addButton(button)
            layout.addWidget(button)
        
        self.buttonGroup.buttonClicked.connect(self._OnCurrentColorChosen)
        
        button.click()
    
    def _OnCurrentColorChosen(self, button):
        print button


class ColoredButtonDialog(QtGui.QDialog):
    def __init__(self, callback, *args, **kwargs):
        super(ColoredButtonDialog, self).__init__(*args, **kwargs)
        layout = QtGui.QHBoxLayout()
        self.setLayout(layout)
        self.chooser = ColoredButtonGroup(8)
        self.chooser.currentColorChosen.connect(callback)
        layout.addWidget(self.chooser)

class Target(object):
    def colorize(self, color):
        print color

target = Target()
chooserdialog = ColoredButtonDialog(target.colorize)
chooserdialog.exec_()
