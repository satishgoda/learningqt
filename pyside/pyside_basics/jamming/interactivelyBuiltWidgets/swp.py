from PySide import QtGui
from PySide import QtCore


class InteractivelyBuiltWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(InteractivelyBuiltWidget, self).__init__(parent)


self = InteractivelyBuiltWidget()

self.pprepImportWidget = InteractivelyBuiltWidget()
self.pprepImportWidget.mainLayout = QtGui.QVBoxLayout()
self.pprepImportWidget.setLayout(self.pprepImportWidget.mainLayout)
self.pprepImportWidget.label = QtGui.QLabel("You are using the published pprep. Good job!")
self.pprepImportWidget.mainLayout.addWidget(self.pprepImportWidget.label)


self.updatedShotEntitiesWidget = InteractivelyBuiltWidget()
self.updatedShotEntitiesWidget.mainLayout = QtGui.QVBoxLayout()
self.updatedShotEntitiesWidget.setLayout(self.updatedShotEntitiesWidget.mainLayout)
self.updatedShotEntitiesWidget.label = QtGui.QLabel("The following asset instances were added to your shot")
self.updatedShotEntitiesWidget.details = QtGui.QLabel("wolf3, wolf_club3, rabbit_small2")
self.updatedShotEntitiesWidget.action = QtGui.QPushButton("Update scene")
self.updatedShotEntitiesWidget.mainLayout.addWidget(self.updatedShotEntitiesWidget.label)
self.updatedShotEntitiesWidget.mainLayout.addWidget(self.updatedShotEntitiesWidget.details)
self.updatedShotEntitiesWidget.mainLayout.addWidget(self.updatedShotEntitiesWidget.action)

self.updatedSiblingsWidget = InteractivelyBuiltWidget()
self.updatedSiblingsWidget.mainLayout = QtGui.QVBoxLayout()
self.updatedSiblingsWidget.setLayout(self.updatedSiblingsWidget.mainLayout)
self.updatedSiblingsWidget.label = QtGui.QLabel("<h3>The following sibling asset instances were added to your shot</h3>")
self.updatedSiblingsWidget.details = QtGui.QLabel("wolf4, wolf_club4, rabbit_small3, rabbit_small4")
self.updatedSiblingsWidget.action = QtGui.QPushButton("Update scene")
self.updatedSiblingsWidget.mainLayout.addWidget(self.updatedSiblingsWidget.label)
self.updatedSiblingsWidget.mainLayout.addWidget(self.updatedSiblingsWidget.details)
self.updatedSiblingsWidget.mainLayout.addWidget(self.updatedSiblingsWidget.action)


self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

self.show()

self.setWindowTitle("Sync With Upstream")

self.mainLayout = QtGui.QVBoxLayout()

self.setLayout(self.mainLayout)

self.mainLayout.addWidget(self.pprepImportWidget)
self.mainLayout.addWidget(self.updatedShotEntitiesWidget)

currentText = self.updatedShotEntitiesWidget.label.text()
self.updatedShotEntitiesWidget.label.setText("<h3>{0}</h3>".format(currentText))

self.mainLayout.addWidget(self.updatedSiblingsWidget)


self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
self.mainLayout.update()
self.adjustSize()

self.updatedShotEntitiesWidget.mainLayout.setDirection(QtGui.QBoxLayout.Direction.LeftToRight)
self.updatedShotEntitiesWidget.mainLayout.setDirection(QtGui.QBoxLayout.Direction.TopToBottom)

self.updatedShotEntitiesWidget.action.setFixedWidth(200)
self.updatedSiblingsWidget.action.setFixedWidth(200)

self.mainLayout.update()
self.adjustSize()
