
from PySide.QtGui import QWidget, QPushButton, QAction
from PySide.QtGui import QVBoxLayout


widget = QWidget()

layout = QVBoxLayout(widget)

pb1 = QPushButton("Tool instance 1")
pb2 = QPushButton("Tool instance 2")

layout.addWidget(pb1)
layout.addWidget(pb2)

widget.show()

selectionChanged = QAction(widget)

def updateObservers(selectionChanged):
    def _doUpdate():
        for observer in selectionChanged.associatedWidgets():
            observer.setEnabled(state)
    return _doUpdate
            
selectionChanged.triggered.connect(updateObservers(selectionChanged))

selectionChanged.associatedWidgets()

pb1.addAction(selectionChanged)

selectionChanged.associatedWidgets()

pb2.addAction(selectionChanged)

selectionChanged.associatedWidgets()

state = False

selectionChanged.trigger()

state = True

selectionChanged.trigger()