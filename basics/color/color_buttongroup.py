class ColoredButtonGroup(QtGui.QGroupBox):
    def __init__(self, numColBut, *args, **kwargs):
        super(ColoredButtonGroup, self).__init__(*args, **kwargs)
        self.numColBut = numColBut

        self.buttonGroup = QtGui.QButtonGroup()
        self.buttonGroup.setExclusive(True)
        
        layout = QtGui.QHBoxLayout()
        layout.setSpacing(1)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        
        for _ in range(self.numColBut):
            randomColor = getRandomQtColor()
            button = ColoredButton(randomColor)
            self.buttonGroup.addButton(button)
            layout.addWidget(button)
        
        self.buttonGroup.buttonClicked.connect(self._OnCurrentColorChosen)
        
        button.click()
    
    def _OnCurrentColorChosen(self, button):
        print button.getColor()
