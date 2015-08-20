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
    created = QPushButton()
    created.setText("{0} @ {1}".format(name, hex(id(created))))
    createdLayout.addWidget(created)
    doneButton.hide()
    nameToCreate.hide()
    createButton.show()
    
doneButton.clicked.connect(doneCreating)

nameToCreate.setMinimumWidth(150)

widget.adjustSize()

#button = createdLayout.takeAt(createdLayout.count()-2).widget()

#createdLayout.insertWidget(0, button)

#button = createdLayout.takeAt(0).widget()

#button.text()

widget.adjustSize()

#button.deleteLater()

#createdLayout.count()

#createdButtons = map(lambda index: createdLayout.itemAt(index).widget(), range(createdLayout.count()))

#createdButtons

#createLayout.spacing()

#createLayout.setSpacing(0)
createLayout.setSpacing(3)
createdLayout.setSpacing(1)
layout.setSpacing(3)

#createdLayout.takeAt(createdLayout.count()-1).widget().deleteLater()

#widget.show()

#toremove = createdLayout.itemAt(createdLayout.count()-1).widget()
#createdLayout.removeWidget(toremove)
#toremove.deleteLater()
#createdLayout.itemAt(0)

def deleteCreated(toremove, tlayout):
    def delete():
        parent = toremove.parent()
        tlayout.removeWidget(toremove)
        toremove.deleteLater()
        parent.adjustSize()
    return delete

def postCreate():
    lastCreatedIndex = createdLayout.count()-1
    lastCreated = createdLayout.itemAt(lastCreatedIndex).widget()
    lastCreated.clicked.connect(deleteCreated(lastCreated, createdLayout))

doneButton.clicked.connect(postCreate)

widget.raise_()

children = QPushButton("children")
layout.addWidget(children)

def printChildren():
    from pprint import pprint
    pprint(widget.children())
    
children.clicked.connect(printChildren)

#createdLayout.update()
#createdLayout.invalidate()
#widget.adjustSize()

#layout.children()

#widget.children()

#widget

#id(widget)
#hex(id(widget))

#layout.count()

#layout.children()

#widget.children()

#widget.findChild(QPushButton, doneButton)

#widget.deleteLater()
