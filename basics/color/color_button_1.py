class ColoredButton(QtGui.QPushButton):
    def __init__(self, color, *args, **kwargs):
        super(ColoredButton, self).__init__(*args, **kwargs)
        self.color_ = color
        colorName = self.color_.name()

        self.setStyleSheet("""
        QPushButton {background-color: %s; color: black; border: none;}
        QPushButton:checked {background-color: %s; color: black; border: 1px solid #222222;}
        """ % (colorName, colorName))
        
        self.setToolTip(self.color_.name())

    def _onToggled(self, checked):
        dimension = 32 if checked else 16
        self.setWidth(dimension)
        self.setHeight(dimension)
