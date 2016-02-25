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


class SelectionChanged(QAction):
    def __init__(self, widget):
        super(SelectionChanged, self).__init__(widget)
        self.triggered.connect(self.notifyAll)
        self.context = Context()

    def updateContext(self, value):
        self.context.state = value
        self.trigger()

    def notifyAll(self):
        for subscriber in self.subscribers:
            subscriber.refresh(self.context)

    @property
    def subscribers(self):
        return self.associatedWidgets()

    def addSubscriber(self, subscriber):
        subscriber.addAction(self)
    

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
        self.onSelectionChanged.addSubscriber(tool)
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


#######


toolbar.onSelectionChanged.updateContext(False)

#######

toolbar.onSelectionChanged.updateContext(True)

#######
