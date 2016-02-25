#######

from PySide.QtGui import QWidget, QPushButton, QAction
from PySide.QtGui import QHBoxLayout

#######


class Context(object):
    def __init__(self):
        self.state = False
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        if not isinstance(value, bool):
            raise ValueError("Invalid state")
        self._state = value

#######


ctx = Context()

#######


print Context.__dict__['state']

#######


print ctx.__dict__

#######

try:
    ctx.state = 1
except ValueError as e:
    print e
    raise e

#######

ctx.state = True

#######

print ctx.__dict__

#######


class SelectionChanged(QAction):
    def __init__(self, widget):
        super(SelectionChanged, self).__init__(widget)
        self.triggered.connect(self.timeToInform)
        self.context = Context()
        
    def inform(self, informee):
        informee.addAction(self)

    @property
    def informees(self):
        return self.associatedWidgets()

    def updateContext(self, value):
        self.context.state = value
        self.trigger()

    def timeToInform(self):
        for informee in self.informees:
            informee.refresh(self.context)

    

#######


class Tool(QPushButton):
    def __init__(self, *args):
        super(Tool, self).__init__(*args)
    
    def refresh(self, context):
        self.setEnabled(context.state)

#######


class ToolBar(QWidget):
    def __init__(self, parent=None):
        super(ToolBar, self).__init__(parent)
        self.onSelectionChanged = SelectionChanged(self)
        self.tools = []
        self._setupUi()
    
    def _setupUi(self):
        layout = QHBoxLayout()
        layout.addStretch()
        self.setLayout(layout)
        self.setMinimumHeight(40)
        self.setMaximumHeight(40)
    
    def addTool(self, name):
        tool = Tool(name)
        self.onSelectionChanged.inform(tool)
        self.tools.append(tool)
        
        layout = self.layout()
        layout.insertWidget(layout.count()-1, tool)

#######


toolbar = ToolBar()

#######


toolbar.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

toolbar.show()


#######


toolbar.addTool("Tool 1")

#######


toolbar.addTool("Tool 2")

#######


try:
    toolbar.onSelectionChanged.updateContext(1)
except ValueError as e:
    print e
    raise

"""
>>> (executing lines 139 to 145 of "qaction.py")
Invalid state
Traceback (most recent call last):
  File "C:\Users\looney\Documents\maya\scripts\learning\pyside\qaction.py", line 145, in <module>
    raise e
ValueError: Invalid state

>>> (executing lines 139 to 145 of "qaction.py")
Invalid state
Traceback (most recent call last):
  File "C:\Users\looney\Documents\maya\scripts\learning\pyside\qaction.py", line 142, in <module>
    toolbar.onSelectionChanged.updateContext(1)
  File "C:\Users\looney\Documents\maya\scripts\learning\pyside\qaction.py", line 71, in updateContext
    self.context.state = value
  File "C:\Users\looney\Documents\maya\scripts\learning\pyside\qaction.py", line 20, in state
    raise ValueError("Invalid state")
ValueError: Invalid state
"""

#######

toolbar.onSelectionChanged.updateContext(True)

#######
