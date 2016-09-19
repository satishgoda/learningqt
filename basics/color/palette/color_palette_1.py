palette = self.palette()

textBrush = palette.buttonText()

textBrush.setColor(QColor(255, 0, 0))

palette.setBrush(QPalette.ColorGroup.Normal, QPalette.ColorRole.ButtonText, textBrush)

textBrush.setColor(QtGui.QColor(175, 0, 0))

palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, textBrush)

self.setPalette(palette)
