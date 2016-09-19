##

palette = self.palette()

brush = palette.buttonText()

brush.setColor(QtGui.QColor(255, 0, 0))
palette.setBrush(QtGui.QPalette.ColorGroup.Normal, QtGui.QPalette.ColorRole.ButtonText, brush)

brush.setColor(QtGui.QColor(175, 0, 0))
palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)

self.setPalette(palette)

##

brush = palette.window()

brush.setColor(QtGui.QColor(0, 255, 0))
palette.setBrush(QtGui.QPalette.ColorGroup.Normal, QtGui.QPalette.ColorRole.Window, brush)

brush.setColor(QtGui.QColor(0, 175, 0))
palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)

self.setPalette(palette)
