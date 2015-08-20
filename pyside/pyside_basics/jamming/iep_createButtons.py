from PySide.QtGui import QPushButton, QAction, QMenu, QWidget, QLabel, QLineEdit
from PySide.QtGui import QVBoxLayout, QHBoxLayout

widget = QWidget()

widget.show()

layout = QVBoxLayout()

widget.setLayout(layout)

createLayout = QHBoxLayout()

layout.addLayout(createLayout)

createButton = QPushButton("Create")

createLayout.addWidget(createButton)

createLayout.addStretch()

layout.addStretch()

doneButton = QPushButton("Done")
doneButton.setParent(widget)

createLayout.insertWidget(0, doneButton)

doneButton.hide()
createButton.hide()
doneButton.show()
doneButton.hide()
createButton.show()

nameToCreate = QLineEdit()
nameToCreate.setParent(widget)

createLayout.insertWidget(createLayout.count()-2, nameToCreate)

doneButton.hide()
nameToCreate.hide()

def doCreate():
    createButton.hide()
    doneButton.show()
    nameToCreate.show()

createButton.clicked.connect(doCreate)

createdLayout = QVBoxLayout()
layout.insertLayout(layout.count()-1, createdLayout)

def doneCreating():
    name = nameToCreate.text()
    created = QPushButton(name)
    createdLayout.addWidget(created)
    doneButton.hide()
    nameToCreate.hide()
    createButton.show()
    
doneButton.clicked.connect(doneCreating)

nameToCreate.setMinimumWidth(150)

widget.adjustSize()

button = createdLayout.takeAt(createdLayout.count()-2).widget()

createdLayout.insertWidget(0, button)

button = createdLayout.takeAt(0).widget()

button.text()

widget.adjustSize()

button.deleteLater()

createdLayout.count()

createdButtons = map(lambda index: createdLayout.itemAt(index).widget(), range(createdLayout.count()))

createdButtons

createLayout.spacing()

createLayout.setSpacing(0)
createLayout.setSpacing(3)

createdLayout.setSpacing(1)

layout.setSpacing(3)

createdLayout.takeAt(createdLayout.count()-1).widget().deleteLater()

def deleteCreated(index, layout):
    def delete():
        widget = layout.takeAt(index).widget()
        widget.deleteLater()
    return delete

def postCreate():
    lastCreatedIndex = createdLayout.count()-1
    lastCreated = createdLayout.itemAt(lastCreatedIndex).widget()
    lastCreated.clicked.connect(deleteCreated(lastCreatedIndex, createdLayout))

doneButton.clicked.connect(postCreate)

widget.deleteLater()