from PySide import QtGui
from PySide import QtCore


##

class CustomAction(QtGui.QAction):
    def __init__(self, message, *args, **kwargs):
        super(CustomAction, self).__init__(*args, **kwargs)
        self.message = message
        self.triggered.connect(self.callback)
        self.setText(message)

    def setEnabled(self, state):
        for widget in self.associatedWidgets():
            if isinstance(widget, CustomButton):
                widget.setEnabled(state)
        super(CustomAction, self).setEnabled(state)
    
    def callback(self):
        print self.message

class CustomButton(QtGui.QPushButton):
    def __init__(self, action, *args, **kwargs):
        super(CustomButton, self).__init__(*args, **kwargs)
        self.addAction(action)
        self.setText(action.message)
        self.clicked.connect(self.callback)
    
    def callback(self):
        self.actions()[0].trigger()
        
        
##

w = QtGui.QWidget()

a = CustomAction('new item', w)
b = CustomAction('rename item', w)
c = CustomAction('edit item', w)

pba = CustomButton(a)
pbb = CustomButton(b)
pbc = CustomButton(c)

w.setLayout(QtGui.QVBoxLayout())

w.layout().addWidget(pba)
w.layout().addWidget(pbb)
w.layout().addWidget(pbc)

m = QtGui.QMenu()

m.addActions([a, b, c])

pbd = QtGui.QPushButton("Choose item action")


pbd.setMenu(m)

w.layout().addWidget(pbd)

w.show()

##

c.setEnabled(False)
c.setEnabled(True)
