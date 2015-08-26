
from PySide.QtGui import QWidget, QPushButton, QAction
from PySide.QtGui import QHBoxLayout


class Context(object):
    def __init__(self):
        self.state = False


class SelectionChanged(QAction):
    def __init__(self, widget):
        super(SelectionChanged, self).__init__(widget)
        self.triggered.connect(self.timeToInform)
        self.context = Context()
    
    @property
    def informees(self):
        return self.associatedWidgets()
    
    def inform(self, informee):
        informee.addAction(self)

    def updateContext(self, value):
        self.context.state = value
        self.trigger()
    
    def timeToInform(self):
        for informee in self.informees:
            informee.refresh(self.context)


class Tool(QPushButton):
    def __init__(self, *args):
        super(Tool, self).__init__(*args)
    
    def refresh(self, context):
        self.setEnabled(context.state)


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


toolbar = ToolBar()
toolbar.show()

toolbar.addTool("Tool 1")
toolbar.addTool("Tool 2")

toolbar.onSelectionChanged.updateContext(False)
toolbar.onSelectionChanged.updateContext(True)