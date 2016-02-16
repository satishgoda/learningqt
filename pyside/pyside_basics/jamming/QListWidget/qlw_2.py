from odwgui import QtGui
from odwgui import QtCore

widget = QtGui.QListWidget()

widget.show()

for index in range(1, 16):
  widget.addItem("{0}".format(index))

widget.setSelectionMode(QtGui.QAbstractItemView.SelectionMode.ExtendedSelection)

widget.selectAll()

for index, item in enumerate(widget.selectedItems(), 1):
    print item.text()
    item.setData(QtCore.Qt.UserRole, {index: "Item {0}".format(index)})
    
items = widget.selectedItems()

try:
    item = items[-1]
except IndexError as e:
    print "Nothing selected"
else:
    print item.text()
    print item.data(QtCore.Qt.DisplayRole)
    print item.data(QtCore.Qt.UserRole)

widget.selectAll()    

for item in widget.selectedItems():
    data = item.data(QtCore.Qt.UserRole)
    print type(data), data
    
