widget = QtGui.QListWidget()

widget.show()

widget.addItem("1")
widget.addItem("2")
widget.addItem("3")

widget.selectionMode()

widget.setSelectionMode(QtGui.QAbstractItemView.SelectionMode.ExtendedSelection)

widget.selectedItems()

for item in widget.selectedItems():
    print item.text()
