from PySide import QtGui


class Data(object):
    def __init__(self):
        self.requiredNames = "A B C D E".split(' ')
        self.availableActions = "Set Select Delete".split(' ')
    
    def Set(self, name):
        print "setting ", name
    
    def Select(self, name):
        print "selecting ", name

    def Delete(self, name):
        print "deleting ", name

class ActionButton(QtGui.QPushButton):
    delegateActionSignal = QtCore.Signal((str, str))

    def __init__(self, itemName, actionName, parent=None):
        super(ActionButton, self).__init__(parent)
        self.itemName = itemName
        self.actionName = actionName
        self.clicked.connect(self._delegate)
        self.setText(self.actionName)
    
    def _delegate(self):
        self.delegateActionSignal.emit(self.itemName, self.actionName)


# def delegated(itemName, actionName):
#     print itemName, actionName
# 
# self = ActionButton('A', 'Set')
# self.delegateActionSignal.connect(delegated)
# self.show()

class DataUIWidget(QtGui.QWidget):
    def __init__(self, data, parent=None):
        super(DataUIWidget, self).__init__(parent)
        self.data = data
        self._setupUI()

    def handleAction(self, itemName, actionName):
        print itemName, actionName

    def _setupUI(self):
        layout = QtGui.QGridLayout()
        self.setLayout(layout)
        
        for index, name in enumerate(self.data.requiredNames):
            lbl = QtGui.QLabel(name)
            layout.addWidget(lbl, index, 0)
            for ind, actName in enumerate(self.data.availableActions, 1):
                btn = ActionButton(name, actName)
                btn.delegateActionSignal.connect(self.handleAction)
                layout.addWidget(btn, index, ind)

data = Data()
self = DataUIWidget(data)
self.show()
