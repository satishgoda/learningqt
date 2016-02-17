# http://doc.qt.io/qt-4.8/qlistwidget.html#details
# http://doc.qt.io/qt-4.8/qt.html#ItemDataRole-enum
# http://doc.qt.io/qt-4.8/qt.html#SortOrder-enum

from odwgui import QtGui
from odwgui import QtCore

self = QtGui.QWidget()

self.mainLayout = QtGui.QVBoxLayout()

self.setLayout(self.mainLayout)

self.operationsLayout1 = QtGui.QHBoxLayout()

self.createButton = QtGui.QPushButton("Create gpuCache")

self.operationsLayout1.addWidget(self.createButton)

self.mainLayout.addLayout(self.operationsLayout1)

self.shotEntitiesLayout = QtGui.QVBoxLayout()

self.mainLayout.addLayout(self.shotEntitiesLayout)

self.shotEntitiesWidget = QtGui.QListWidget()
self.shotEntitiesWidget.setSelectionMode(QtGui.QAbstractItemView.SelectionMode.ExtendedSelection)

self.shotEntitiesLayout.addWidget(self.shotEntitiesWidget)

self.siblingLabel = QtGui.QLabel("Update me")

self.mainLayout.addWidget(self.siblingLabel)

self.operationsLayout2 = QtGui.QHBoxLayout()

self.refreshButton = QtGui.QPushButton("Refresh")

self.operationsLayout2.addWidget(self.refreshButton)

self.mainLayout.addLayout(self.operationsLayout2)

self.siblingEntitiesLayout = QtGui.QVBoxLayout()

self.mainLayout.addLayout(self.siblingEntitiesLayout)

self.siblingEntitiesWidget = QtGui.QListWidget()
self.siblingEntitiesWidget.setSelectionMode(QtGui.QAbstractItemView.SelectionMode.ExtendedSelection)

self.siblingEntitiesLayout.addWidget(self.siblingEntitiesWidget)

self.show()

entityMap = OrderedDict()

for key, group in groupby(entities, key=lambda entity: entity.__class__.__name__):
    entityMap[key] = tuple(group)
    
shot_entities = entityMap['ShotEntity']

for sentity in shot_entities:
    item = QtGui.QListWidgetItem(sentity.namespace)
    item.setData(QtCore.Qt.UserRole, sentity)
    self.shotEntitiesWidget.addItem(item)

self.siblingLabel.setText("The following are the GPU Caches from sibling tasks")

sibling_entities = entityMap['SharedShotCachedEntity']

for sientity in sibling_entities:
    item = QtGui.QListWidgetItem("{} [{}]".format(sientity.namespace, sientity.task))
    item.setData(QtCore.Qt.UserRole, sientity)
    self.siblingEntitiesWidget.addItem(item)
    
def refresh():
    items = self.siblingEntitiesWidget.selectedItems()
    
    if not items:
        io.write("Warning: Nothing selected")
        return
        
    for item in items:
        sientity = item.data(QtCore.Qt.UserRole)
        sientity.operation()

self.refreshButton.clicked.connect(refresh)

self.shotEntitiesWidget.currentItem().text()

self.siblingEntitiesWidget.currentItem().text()

self.siblingEntitiesWidget.currentItem() is self.siblingEntitiesWidget.selectedItems()[-1]

self.shotEntitiesWidget.setSortingEnabled(True)
self.shotEntitiesWidget.sortItems()

self.siblingEntitiesWidget.setSortingEnabled(True)
self.siblingEntitiesWidget.sortItems()
self.siblingEntitiesWidget.sortItems(QtCore.Qt.DescendingOrder)

self.siblingEntitiesWidget.children()
# [
#     <PySide.QtGui.QWidget object at 0x0000008D4DF5AB88>, 
#     <PySide.QtGui.QWidget object at 0x0000008D4DF5E908>, 
#     <PySide.QtGui.QWidget object at 0x0000008D4DF5E848>, 
#     <PySide.QtGui.QStyledItemDelegate object at 0x0000008D4DF5EBC8>,         
#     <PySide.QtCore.QAbstractListModel object at 0x0000008D4DF5E788>, 
#     <PySide.QtGui.QItemSelectionModel object at 0x0000008D4DF5E9C8>
# ]

self.shotEntitiesWidget.children()

self.siblingEntitiesWidget.item(0)
# <PySide.QtGui.QListWidgetItem object at 0x0000008D4DF5E088>

map(self.siblingEntitiesWidget.item, range(self.siblingEntitiesWidget.count()))

self.siblingEntitiesWidget.clearSelection()

matched = self.siblingEntitiesWidget.findItems('slave3', QtCore.Qt.MatchContains)

for match in matched:
    match.setSelected(True)

selModel = self.siblingEntitiesWidget.selectionModel()

selModel.selectedRows()
# [
#     <PySide.QtCore.QModelIndex(0,0,0x8d4eb19a30,QListModel(0x8d4e67db70) )   at 0x0000008D4DF5EBC8>, 
#     <PySide.QtCore.QModelIndex(3,0,0x8d4eb19b70,QListModel(0x8d4e67db70) )   at 0x0000008D4DF5E3C8>
# ]

itemModel = self.siblingEntitiesWidget.model()
# <PySide.QtCore.QAbstractListModel object at 0x0000008D4DF5E588>

itemModel.rowCount()
# 4

self.shotEntitiesWidget.hide()
self.siblingEntitiesWidget.hide()
self.shotEntitiesWidget.show()
self.siblingEntitiesWidget.show()
