from odwgui import QtGui
from odwgui import QtCore

qtw = QtGui.QTreeWidget()

qtw.setSelectionMode(QtGui.QAbstractItemView.SelectionMode.ExtendedSelection)

qtw.show()

from itertools import groupby

for key, group in groupby(entities, key=lambda entity: entity.task):
    qtwtli = QtGui.QTreeWidgetItem()
    qtwtli.setText(0, key)
    qtw.addTopLevelItem(qtwtli)
    for entity in group:
        qtwi = QtGui.QTreeWidgetItem(qtwtli)
        qtwi.setText(0, entity.namespace)
        qtwi.setText(1, entity.task)
        qtwi.setText(2, entity.group)
        qtwi.setText(3, entity.__class__.__name__)
        
si = qtw.selectedItems()[0]

si.childCount()

si.child(0).text(0)
si.child(1).text(0)
si.child(2).text(0)
si.child(3).text(0)

selis = qtw.selectedItems()

for seli in selis:
    print seli.text(0)
    print "\t", seli.parent().text(0)
    
qtw.topLevelItemCount()

qtw.topLevelItem(0).text(0)
qtw.topLevelItem(1).text(0)
qtw.topLevelItem(2).text(0)

si = qtw.selectedItems()[0]

si.setHidden(False)

itemsToHide = qtw.selectedItems()

for si in itemsToHide:
    si.setHidden(True)
    
for i in itemsToHide:
    i.setHidden(False)
    
qtw.findItems('slave3', QtCore.Qt.MatchContains)[0].isHidden()

i.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

for index in range(qtw.topLevelItemCount()):
    tli = qtw.topLevelItem(index)
    tli.setCheckState(0, QtCore.Qt.CheckState.Unchecked)
