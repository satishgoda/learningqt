from PySide import QtGui

self = QtGui.QColorDialog()

self.setOption(QtGui.QColorDialog.ColorDialogOption.ShowAlphaChannel, True)

self.exec_()

##

selectedColor = self.selectedColor()

print selectedColor.toTuple()

print selectedColor.name()

##


color =  QtGui.QColorDialog.getColor()

print color

##

self = QtGui.QColorDialog()

print self.open()

print self.selectedColor()
