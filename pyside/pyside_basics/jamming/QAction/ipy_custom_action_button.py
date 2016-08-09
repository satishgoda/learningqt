from collections import OrderedDict
from functools import partial

from PySide import QtCore
from PySide import QtGui

##

class CustomAction(QtGui.QAction):
    def __init__(self, message, *args, **kwargs):
        super(CustomAction, self).__init__(*args, **kwargs)
        self.message = message
        self.triggered.connect(self.callback)
    
    def callback(self):
        print self.message, self.sender(), self.senderSignalIndex()

class CustomButton(QtGui.QPushButton):
    def __init__(self, *args, **kwargs):
        super(CustomButton, self).__init__(*args, **kwargs)
        self.clicked.connect(self.callback)
    
    def callback(self):
        print self.text()
        
        for action in self.actions():
            action.activate(QtGui.QAction.ActionEvent.Trigger)

##

mw = QtGui.QMainWindow()

customAction1 = CustomAction("Action 1", mw)
customAction2 = CustomAction("Action 2", mw)

button = CustomButton("Click me")

print customAction1, button

button.show()

##

button.addAction(customAction1)

##

button.addAction(customAction2)

##

button.removeAction(customAction1)

##

button.removeAction(customAction2)

##

button.addActions([customAction1, customAction2])
